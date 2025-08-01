# Generated by Django 5.2.3 on 2025-07-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campaign",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("target_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
    ]
