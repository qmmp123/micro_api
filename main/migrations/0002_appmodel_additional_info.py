# Generated by Django 2.2.7 on 2020-05-07 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appmodel',
            name='additional_info',
            field=models.TextField(default=''),
        ),
    ]
