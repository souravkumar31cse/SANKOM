# Generated by Django 3.2.9 on 2021-12-17 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20211217_1554'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='zip_code',
        ),
    ]
