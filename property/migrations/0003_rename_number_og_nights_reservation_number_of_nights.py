# Generated by Django 5.0.2 on 2025-03-20 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='number_og_nights',
            new_name='number_of_nights',
        ),
    ]
