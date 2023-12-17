# Generated by Django 4.2.5 on 2023-10-15 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='location',
            field=models.CharField(max_length=255),
        ),
    ]
