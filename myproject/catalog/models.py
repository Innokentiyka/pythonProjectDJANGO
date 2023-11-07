from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение (превью)')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name

created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='blog_previews/')
    created_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии')
    version_title = models.CharField(max_length=200, verbose_name='Название версии')
    is_current = models.BooleanField(default=False, verbose_name='Текущая версия')

    def str(self):
        return f"{self.version_title} (версия {self.version_number}) для продукта {self.product.name}"

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'