# Generated by Django 4.2.16 on 2024-11-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_slot_date_timeslot_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
