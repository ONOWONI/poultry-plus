# Generated by Django 4.1.1 on 2023-01-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base_app", "0009_alter_expenses_date_alter_income_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="animal",
            name="modified_aat",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
