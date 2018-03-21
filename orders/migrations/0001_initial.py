# Generated by Django 2.0.1 on 2018-02-08 19:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(help_text='Provide your chowk, ward no. and house number if possible', max_length=100)),
                ('nearest_place', models.CharField(blank=True, help_text='Nearest place from you that everyone knows in your area', max_length=30)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
    ]