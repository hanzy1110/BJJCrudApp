# Generated by Django 4.2.4 on 2023-08-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BJJCrudAPP', '0005_rename_clase_student_age_class_student_weight_class_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('m', 'Masculino'), ('f', 'Femenino')], max_length=20, null=True, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='student',
            name='age_class',
            field=models.CharField(max_length=50, verbose_name='Division Edad'),
        ),
        migrations.AlterField(
            model_name='student',
            name='weight_class',
            field=models.CharField(max_length=50, null=True, verbose_name='Division Peso'),
        ),
    ]
