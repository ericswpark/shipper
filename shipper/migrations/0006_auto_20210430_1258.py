# Generated by Django 3.2 on 2021-04-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipper', '0005_auto_20210428_0745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='build',
            name='gapps',
        ),
        migrations.AddField(
            model_name='build',
            name='variant',
            field=models.TextField(default='unknown', help_text='One of the following variants: gapps, vanilla, goapps, foss', max_length=20),
            preserve_default=False,
        ),
    ]