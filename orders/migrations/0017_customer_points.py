# Generated by Django 2.0.1 on 2018-03-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_ordereditem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
