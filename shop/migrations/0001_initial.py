# Generated by Django 2.0.1 on 2018-02-02 15:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=25)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=35)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=110)),
                ('duration', models.DurationField(default=datetime.timedelta(30))),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=350)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percent', models.FloatField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('image3', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('image4', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('stock', models.PositiveIntegerField()),
                ('for_sale', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3)),
                ('total_sells', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category')),
                ('manufactured_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.Manufacturer')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.Offer')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60)),
                ('total_sells', models.PositiveIntegerField(default=0)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=25)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='shop.Category')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.Subcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
