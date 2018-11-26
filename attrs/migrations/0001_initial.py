# Generated by Django 2.1.3 on 2018-11-26 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Unit",
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
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="name"
                    ),
                ),
                ("symbol", models.CharField(max_length=10, verbose_name="symbol")),
            ],
        )
    ]
