# Generated by Django 3.1.1 on 2021-09-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20210917_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='carts.SaleProduct'),
        ),
    ]
