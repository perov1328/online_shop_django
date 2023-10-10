
from django.core.management import BaseCommand
from catalog.models import Category

class Command(BaseCommand):
    """
    Команда для записи категорий в БД
    """
    def handle(self, *args, **options):
        categories_list = [
            {'name': 'Клавиатура'},
            {'name': 'Компьютерные мыши'},
            {'name': 'Мониторы'}
        ]

        Category.objects.all().delete()

        categories_for_create = []
        for category in categories_list:
            categories_for_create.append(
                Category(**category)
            )

        Category.objects.bulk_create(categories_for_create)
