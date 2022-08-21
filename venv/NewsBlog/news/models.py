from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
   title = models.CharField(max_length=150, verbose_name='Заголовок')
   preview = models.CharField(max_length=500, verbose_name='Краткое описание')
   content = models.TextField(blank=True, verbose_name='Контент')
   link = models.CharField(max_length=150, verbose_name='Ссылка', blank=True)
   photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
   author = models.ForeignKey(User ,on_delete=models.CASCADE,null=True, verbose_name='Автор')

   def get_absolute_url(self):
      return reverse('view_news', kwargs={"pk": self.pk})

   def __str__(self):
      return self.title

   class Meta:
      verbose_name = 'Новость'
      verbose_name_plural = 'Новости'
      ordering = ['-id']

