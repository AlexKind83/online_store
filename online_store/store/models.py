from django.db import models
from django.urls import reverse


from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']  # сортировка
        indexes = [models.Index(fields=['name']),]  # поиск
        verbose_name = 'category'  # чтобы убрать не красивое добавление 's'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Автоматизация url адресов"""
        return reverse('store:category_slug', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Товар')
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='изменен')

    class Meta:
        ordering = ['name']  # сортировка записи
        indexes = [models.Index(fields=['id', 'slug']),  # поиск по индексам
                   models.Index(fields=['name']),
                   models.Index(fields=['-created']),]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Автоматизация url адресов"""
        return reverse('store:product_detail', args=[self.pk, self.slug])



