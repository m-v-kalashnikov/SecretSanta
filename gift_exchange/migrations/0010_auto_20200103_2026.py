# Generated by Django 3.0.1 on 2020-01-03 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gift_exchange', '0009_auto_20200103_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftexchange',
            name='creator',
        ),
        migrations.AddField(
            model_name='giftexchange',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
