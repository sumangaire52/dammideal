# Generated by Django 2.0.1 on 2018-02-08 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180209_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditem',
            name='name',
        ),
    ]
