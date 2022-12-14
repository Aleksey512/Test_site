# Generated by Django 4.1 on 2022-08-20 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0006_alter_nameautor_options_news_name_autor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='name_autor',
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(blank=True, max_length=150, verbose_name='Ссылка'),
        ),
        migrations.DeleteModel(
            name='NameAutor',
        ),
    ]
