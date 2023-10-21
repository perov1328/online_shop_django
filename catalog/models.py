from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    Модель для категорий
    """
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f"Категория: {self.name}"

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """
    Модель для продуктов
    """
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField(verbose_name='Цена за покупку')
    date_of_creation = models.DateField(verbose_name='Дата создания')
    date_of_last_modification = models.DateTimeField(auto_now_add=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f"{self.category} (Категория: {self.category})"

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name',)    # Сортировка по наименованию продукта

class Blog(models.Model):
    """
    Модель для блоговой записи
    """
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')
    content = models.TextField(**NULLABLE, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Превью')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'Блог: {self.title}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('title',)  # Сортировка по наименованию продукта
