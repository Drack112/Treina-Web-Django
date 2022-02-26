# Generated by Django 2.1.3 on 2018-11-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("data_nascimento", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                ("profissao", models.CharField(max_length=50)),
                (
                    "sexo",
                    models.CharField(
                        choices=[
                            ("F", "Feminino"),
                            ("M", "Masculino"),
                            ("N", "Nenhuma das opções"),
                        ],
                        max_length=1,
                    ),
                ),
            ],
        )
    ]
