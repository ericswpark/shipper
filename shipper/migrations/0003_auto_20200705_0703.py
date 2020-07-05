# Generated by Django 3.0.7 on 2020-07-05 07:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipper', '0002_build_processed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='maintainers',
            field=models.ManyToManyField(blank=True, help_text='Choose the maintainers working on this device. Multiple maintainers can be selected.<br>', related_name='devices', to=settings.AUTH_USER_MODEL),
        ),
    ]