# Generated by Django 3.2.11 on 2022-01-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_rest_resetpassword", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="resetpasswordtoken",
            name="origin",
            field=models.CharField(
                blank=True, default="", max_length=256, verbose_name="Request Origin"
            ),
        ),
    ]
