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
