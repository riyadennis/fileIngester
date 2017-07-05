from django.core.management.base import BaseCommand
from database_schema.models import  Product
import csv


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        self.stdout.write("Hello World")
        self.ingestFile()

    def ingestFile(self):
        file = open('data/products.csv', 'r')
        reader = csv.DictReader(file)
        for row in reader:
            product = Product()
            product.description = row['description']
            product.sku = row['sku']
            product.store_id = row['store_id']
            product.is_promotion = row['is_promotion']
            product.save()
        file.close()
