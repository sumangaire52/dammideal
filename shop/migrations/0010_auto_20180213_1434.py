# Generated by Django 2.0.1 on 2018-02-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20180213_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='available_colors',
            field=models.ManyToManyField(to='shop.Color'),
        ),
    ]