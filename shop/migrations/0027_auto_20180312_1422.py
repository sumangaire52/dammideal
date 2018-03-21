# Generated by Django 2.0.1 on 2018-03-12 08:37

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20180218_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=100, size=[1024, 720], upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=100, size=[1024, 720], upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=100, size=[1024, 720], upload_to='products/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=100, size=[1024, 720], upload_to='products/%Y/%m/%d'),
        ),
    ]
