# Generated by Django 4.2.6 on 2023-10-26 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("measurement", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="measurement",
            name="sensor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sensor",
                to="measurement.sensor",
                verbose_name="Модель датчика",
            ),
        ),
    ]
