# Generated by Django 3.1.1 on 2021-09-28 16:43

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
