# Generated by Django 3.0.8 on 2020-07-13 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='condition',
            field=models.CharField(choices=[('bad', 'Bad'), ('good', 'Good')], default='good', max_length=20),
        ),
    ]