# Generated by Django 3.0.7 on 2020-07-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]