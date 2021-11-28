# Generated by Django 3.2.7 on 2021-11-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_subscribe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='volunteer_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
