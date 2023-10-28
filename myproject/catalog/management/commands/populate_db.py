from django.core.management.base import BaseCommand
from django.core.management import call_command
from myproject.catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Clear old data and populate database with new data from fixtures'

    def handle(self, *args, **kwargs):
        # Зачистка старых данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка данных из фикстуры
        call_command('loaddata', 'catalog_fixture.json')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
