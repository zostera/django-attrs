# Generated by Django 2.1.3 on 2018-11-27 09:55

import attrs.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("app", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Visit",
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
                ("name", models.CharField(max_length=100)),
                ("attrs", attrs.fields.AttrsField(default=dict, editable=False)),
                (
                    "protocol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.Protocol"
                    ),
                ),
            ],
        )
    ]