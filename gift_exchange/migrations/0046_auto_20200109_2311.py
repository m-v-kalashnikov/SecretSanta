# Generated by Django 3.0.1 on 2020-01-09 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_exchange', '0045_auto_20200109_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftexchange',
            name='image',
            field=models.ImageField(blank=True, default='media/img/0000/00/00/gifts-4.jpg', null=True, upload_to='media/img/%Y/%m/%d', verbose_name='Картинка для вида'),
        ),
    ]
