# Generated by Django 4.2.7 on 2023-12-12 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hstem", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="file",
        ),
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "name",
                    models.CharField(
                        db_column="name",
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("is_public", models.BooleanField(default=False)),
                ("type", models.CharField(max_length=50)),
                ("uploaded_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("file", models.FileField(null=True, upload_to="files/")),
                (
                    "title",
                    models.ForeignKey(
                        db_column="title",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="hstem.project",
                    ),
                ),
            ],
        ),
    ]