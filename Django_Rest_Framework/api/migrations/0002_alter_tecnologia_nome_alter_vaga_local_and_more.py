# Generated by Django 4.0.2 on 2022-02-26 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tecnologia",
            name="nome",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="vaga",
            name="local",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="vaga",
            name="salario",
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name="vaga",
            name="tipo_contratacao",
            field=models.CharField(
                choices=[
                    ("CLT", "Empregado registrado pela CLT"),
                    ("PJ", "Pessoa Jurídica"),
                ],
                max_length=3,
            ),
        ),
    ]
