# Generated by Django 3.0.7 on 2020-07-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='codename',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='cpu',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='gpu',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
