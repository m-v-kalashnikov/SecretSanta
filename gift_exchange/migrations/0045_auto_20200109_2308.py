# Generated by Django 3.0.1 on 2020-01-09 21:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gift_exchange', '0044_auto_20200109_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftexchange',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
