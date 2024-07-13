# Generated by Django 5.0.6 on 2024-07-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wezeshaWebPortalCooperative", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cooperative",
            name="id",
        ),
        migrations.AddField(
            model_name="cooperative",
            name="cooperative_id",
            field=models.SmallIntegerField(
                default=1, primary_key=True, serialize=False
            ),
        ),
    ]
