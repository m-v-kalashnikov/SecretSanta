# Generated by Django 3.0.1 on 2020-01-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_exchange', '0012_auto_20200104_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftexchange',
            name='slug',
            field=models.SlugField(max_length=100, unique_for_date=True, verbose_name='Url адрес сбора'),
        ),
    ]
