# Generated by Django 3.0.5 on 2020-04-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20200409_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
