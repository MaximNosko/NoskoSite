from django.db import models

# Create your models here.
class News(models.Model):
    title=models.CharField(verbose_name="Заголовок новости",max_length=150)
    content = models.CharField(verbose_name="Текст",max_length=500, blank=True)
    create_at=models.DateTimeField(verbose_name="Дата создания",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновления", auto_now=True)
    photo=models.ImageField(verbose_name="Изображения",upload_to="photos/%Y/%m/%d/")
    is_published=models.BooleanField(verbose_name="Публиковать",default=True)