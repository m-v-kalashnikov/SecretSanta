# Generated by Django 3.0.1 on 2020-01-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_exchange', '0040_auto_20200109_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftexchange',
            name='image',
            field=models.ImageField(blank=True, default='media/img/0000/00/00/gifts-3.jpg', null=True, upload_to='media/img/%Y/%m/%d', verbose_name='Картинка для вида'),
        ),
    ]
