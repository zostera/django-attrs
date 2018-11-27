# Generated by Django 2.1.3 on 2018-11-26 10:49

import django.db.models.deletion
from django.db import migrations, models

import attrs.fields


class Migration(migrations.Migration):

    dependencies = [("attrs", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Attribute",
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
                (
                    "type",
                    attrs.fields.AttributeTypeField(
                        choices=[
                            (attrs.fields.ATTRIBUTE_TYPE_TEXT, "text"),
                            (attrs.fields.ATTRIBUTE_TYPE_BOOLEAN, "boolean"),
                            (attrs.fields.ATTRIBUTE_TYPE_INTEGER, "integer"),
                            (attrs.fields.ATTRIBUTE_TYPE_FLOAT, "float"),
                            (attrs.fields.ATTRIBUTE_TYPE_DATE, "date"),
                            (attrs.fields.ATTRIBUTE_TYPE_TIME, "time"),
                        ],
                        max_length=100,
                        verbose_name="type",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attrs.Unit",
                        verbose_name="unit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Choice",
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
                    "value",
                    models.CharField(
                        blank=True, db_index=True, max_length=100, verbose_name="value"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, db_index=True, max_length=100, verbose_name="name"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "sort_order",
                    models.IntegerField(
                        db_index=True, default=0, verbose_name="sort order"
                    ),
                ),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attrs.Attribute",
                    ),
                ),
            ],
            options={"ordering": ["attribute_id", "sort_order", "value", "pk"]},
        ),
    ]
