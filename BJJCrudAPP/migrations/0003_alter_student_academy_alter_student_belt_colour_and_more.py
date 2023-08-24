# Generated by Django 4.2.4 on 2023-08-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BJJCrudAPP', '0002_student_name_student_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academy',
            field=models.CharField(max_length=50, verbose_name='Academia'),
        ),
        migrations.AlterField(
            model_name='student',
            name='belt_colour',
            field=models.CharField(max_length=20, verbose_name='Faixa'),
        ),
        migrations.AlterField(
            model_name='student',
            name='clase',
            field=models.CharField(max_length=50, verbose_name='Clase'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(verbose_name='Fecha Nacimiento'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_id',
            field=models.CharField(max_length=10, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=50, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='student',
            name='weight',
            field=models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Peso'),
        ),
    ]