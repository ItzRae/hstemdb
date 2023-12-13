# Generated by Django 4.2.7 on 2023-12-13 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hstem", "0002_rename_primary_theme_project_cohort_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="create",
            name="title",
            field=models.ForeignKey(
                db_column="title",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hstem.project",
            ),
        ),
    ]