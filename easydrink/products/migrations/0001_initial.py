# Generated by Django 3.1.1 on 2021-08-16 20:39

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('color', models.CharField(choices=[('#FFFFFF', 'WHITE'), ('#000000', 'BLACK'), ('#FF0000', 'RED'), ('#006600', 'GREEN'), ('#0033CC', 'BLUE'), ('#FFCC00', 'YELLOW'), ('#FF9900', 'ORANGE'), ('#9900FF', 'PURPLE'), ('#FF99CC', 'PINK')], max_length=25)),
                ('available', models.CharField(choices=[('A', 'available'), ('U', 'unavailable')], default=('A', 'available'), max_length=1)),
                ('image', models.ImageField(upload_to='')),
                ('department', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products.category')),
            ],
        ),
    ]
