# Generated by Django 2.0.1 on 2018-02-10 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_phonenumber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Phonenumber',
            new_name='Customer',
        ),
    ]
