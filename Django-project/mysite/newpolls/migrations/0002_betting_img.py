# Generated by Django 4.1 on 2022-08-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newpolls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='betting',
            name='img',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
