# Generated by Django 4.2.5 on 2023-11-13 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_alter_reservation_client_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='client_id',
            new_name='client',
        ),
    ]
