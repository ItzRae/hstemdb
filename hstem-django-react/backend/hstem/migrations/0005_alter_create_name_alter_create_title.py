# Generated by Django 4.2.7 on 2023-12-13 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hstem", "0004_alter_create_name_alter_create_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="create",
            name="name",
            field=models.ForeignKey(
                db_column="name",
                default="Student",
                on_delete=django.db.models.deletion.DO_NOTHING,
                primary_key=True,
                related_name="creates",
                serialize=False,
                to="hstem.author",
            ),
        ),
        migrations.AlterField(
            model_name="create",
            name="title",
            field=models.ForeignKey(
                blank=True,
                db_column="title",
                default="A Project",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hstem.project",
            ),
        ),
    ]