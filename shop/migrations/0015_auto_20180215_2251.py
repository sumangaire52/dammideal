# Generated by Django 2.0.1 on 2018-02-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20180215_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='brand_image',
            field=models.ImageField(null=True, upload_to='manufacturers/'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='brand_image',
            field=models.ImageField(null=True, upload_to='vendors/'),
        ),
    ]