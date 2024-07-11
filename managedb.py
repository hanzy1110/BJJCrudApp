import pathlib
import sqlite3
import csv
from itertools import product

import PyPDF2

from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


# 1. Connect to the SQLite database
CSV_FOLDERNAME = pathlib.Path(__file__).parent / "csv"
PDF_FOLDERNAME = pathlib.Path(__file__).parent / "pdfs"
OUTPUT_PDF = pathlib.Path(__file__).parent / "tablas_competencia.pdf"

STYLE = TableStyle(
    [
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ]
)

TABLE_NAME = "BJJCrudAPP_student"
SQL_PATH = pathlib.Path(__file__).parent / "db.sqlite3"

db_connection = sqlite3.connect(SQL_PATH)
cursor = db_connection.cursor()


def build_queries():
    results = {}
    class_queries = {
        "belt_colour": f"SELECT DISTINCT belt_colour FROM {TABLE_NAME}",
        "weight_class": f"SELECT DISTINCT weight_class FROM {TABLE_NAME}",
        "age_class": f"SELECT DISTINCT age_class FROM {TABLE_NAME}",
        "gender": f"SELECT DISTINCT gender FROM {TABLE_NAME}",
    }

    for q, q_val in class_queries.items():
        cursor.execute(q_val)
        results[q] = cursor.fetchall()

    queries = {}
    for belt, weight_class, age_class, gender in product(*list(results.values())):
        belt = belt[0]
        weight_class = weight_class[0]
        age_class = age_class[0]
        gender = gender[0]

        query_str = f"{belt}_{weight_class}_{age_class}_{gender}"
        queries[
            query_str
        ] = f"SELECT * FROM {TABLE_NAME} WHERE `belt_colour`='{belt}' AND `weight_class`='{weight_class}' AND `age_class`='{age_class}' AND `gender`='{gender}'"

    return queries


def get_data(query_str, sql_query):
    cursor.execute(sql_query)
    results = cursor.fetchall()
    csv_filename = CSV_FOLDERNAME / f"{query_str}.csv"

    if results:
        with open(csv_filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            column_names = [description[0] for description in cursor.description]
            csv_writer.writerow(column_names)
            csv_writer.writerows(results)
        return csv_filename

    return None


def write_pdf(query_str, csv_filename):
    data = []
    with open(csv_filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)

    pdf_filename = PDF_FOLDERNAME / f"{query_str}.pdf"

    # Create a PDF document
    page_width, page_height = landscape(letter)
    pdf = SimpleDocTemplate(str(pdf_filename), pagesize=landscape(letter))

    table_data = []
    # Get ReportLab stylesheet for paragraph styling
    styles = getSampleStyleSheet()

    for row in data:
        table_row = []
        for item in row:
            # Create a Paragraph for each cell to handle multi-line text
            table_row.append(Paragraph(item, styles["Normal"]))
        table_data.append(table_row)

    table = Table(table_data, colWidths=[page_width / len(data[0]) for _ in data[0]])
    # Style the table
    table.setStyle(STYLE)
    # Build the PDF document
    pdf.build([table])
    print(f"PDF report has been created: '{pdf_filename}'.")

    return pdf_filename


def main():
    sql_queries = build_queries()
    pdf_filenames = []
    for query_str, sql_query in sql_queries.items():
        print(f"RUNNING_QUERY {query_str}")
        csv_filename = get_data(query_str=query_str, sql_query=sql_query)
        if csv_filename:
            pdf_filenames.append(write_pdf(query_str, csv_filename))

    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Iterate through the PDF files and append them to the merger
    for pdf_file in pdf_filenames:
        pdf_merger.append(pdf_file)

    # Write the merged PDF to the output file
    with open(OUTPUT_PDF, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f"PDF files have been concatenated to '{OUTPUT_PDF}'.")


if __name__ == "__main__":
    main()
    db_connection.close()
    # print(build_queries())
