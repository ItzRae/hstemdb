# Generated by Django 4.2.7 on 2023-12-13 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hstem", "0003_alter_create_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="create",
            name="title",
            field=models.ForeignKey(
                blank=True,
                db_column="title",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="hstem.project",
            ),
        ),
    ]