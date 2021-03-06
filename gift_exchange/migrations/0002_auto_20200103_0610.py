# Generated by Django 3.0.1 on 2020-01-03 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gift_exchange', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftExchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, verbose_name='Url адрес сбора')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price_limit', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Ограничение по сумме')),
                ('max_adorable_date', models.DateTimeField(verbose_name='Дата до которой можно подключится')),
            ],
            options={
                'verbose_name': 'Обмен подарками',
                'verbose_name_plural': 'Обмен подарками',
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Пожелания')),
                ('gift_exchange', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gift_exchange.GiftExchange')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Подарок',
                'verbose_name_plural': 'Подарки',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='organisator_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gift_exchange.GiftExchange'),
        ),
    ]
