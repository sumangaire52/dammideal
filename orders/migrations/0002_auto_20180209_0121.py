# Generated by Django 2.0.1 on 2018-02-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
