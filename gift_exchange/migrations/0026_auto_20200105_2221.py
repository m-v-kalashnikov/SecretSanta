# Generated by Django 3.0.1 on 2020-01-05 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_exchange', '0025_auto_20200105_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftexchange',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/%Y/%m/%d', verbose_name='Картинка для вида'),
        ),
    ]
