from django.core.management.base import BaseCommand

from magazin.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(title='Auto', description='Electro', price=1000, count=2,)
        product.save()
        self.stdout.write(f'{product}')