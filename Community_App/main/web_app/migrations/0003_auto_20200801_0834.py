# Generated by Django 2.0.7 on 2020-08-01 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_auto_20200801_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpage',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='createpage',
            name='location',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='createpage',
            name='organisation',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
