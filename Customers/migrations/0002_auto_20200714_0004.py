# Generated by Django 3.0.8 on 2020-07-13 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_in',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
