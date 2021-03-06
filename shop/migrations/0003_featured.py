# Generated by Django 2.0.1 on 2018-02-06 06:35

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('shop', '0002_carousal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured',
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
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_products', to='shop.Category')),
                ('manufactured_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_products', to='shop.Manufacturer')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_products', to='shop.Offer')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_products', to='shop.Seller')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_products', to='shop.Subcategory')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
