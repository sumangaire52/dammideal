# Generated by Django 2.0.1 on 2018-02-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20180215_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('xxs', 'XXS'), ('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL'), ('xxxl', 'XXXL')], max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='shop.Size'),
        ),
    ]
