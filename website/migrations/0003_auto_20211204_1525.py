# Generated by Django 3.2.7 on 2021-12-04 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20211204_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created_user',
        ),
        migrations.RemoveField(
            model_name='event',
            name='updated_user',
        ),
    ]
