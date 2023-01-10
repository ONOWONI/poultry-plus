# Generated by Django 4.1.1 on 2023-01-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TransactionRef",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tx_ref", models.CharField(default="None", max_length=30)),
                ("owner_id", models.IntegerField()),
            ],
        ),
    ]
