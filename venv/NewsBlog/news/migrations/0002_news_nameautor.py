# Generated by Django 4.1 on 2022-08-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='nameautor',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
    ]
