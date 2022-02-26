# Generated by Django 3.0 on 2019-12-16 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("blog", "0002_auto_20191213_1358")]

    operations = [
        migrations.CreateModel(
            name="Autor",
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
                ("nome", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(model_name="post", name="categoria"),
        migrations.DeleteModel(name="Categoria"),
        migrations.AddField(
            model_name="post",
            name="autor",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="blog.Autor"
            ),
            preserve_default=False,
        ),
    ]
