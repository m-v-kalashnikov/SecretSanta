# Generated by Django 3.0.1 on 2020-01-05 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gift_exchange', '0018_auto_20200105_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='gift_exchange',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gift_exchange.GiftExchange'),
        ),
    ]
