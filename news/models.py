from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=150)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

class Keyword(models.Model):
    title=models.CharField(verbose_name="Наименование",max_length=150)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = "Ключевые слова"

class News(models.Model):
    title=models.CharField(verbose_name="Заголовок новости",max_length=150)
    content = models.CharField(verbose_name="Текст",max_length=500, blank=True)
    create_at=models.DateTimeField(verbose_name="Дата создания",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновления", auto_now=True)
    #photo=models.ImageField(verbose_name="Изображения",upload_to="photos/%Y/%m/%d/",blank=True,null=True)
    is_published=models.BooleanField(verbose_name="Публиковать",default=True)
    #category_id = models.IntegerField(verbose_name="Категория",default=1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    keywords = models.ManyToManyField(Keyword)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"

class Comment(models.Model):
    text=models.CharField(verbose_name="Текст",max_length=150)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"