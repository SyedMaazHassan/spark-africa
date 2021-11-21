# Generated by Django 3.2.7 on 2021-11-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_cause_event_eventcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=256)),
                ('note', models.TextField(max_length=2000)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]