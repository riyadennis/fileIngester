from django.core.management.base import BaseCommand
import csv

class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Django admin custom command poc.'

    def handle(self, *args, **options):
        self.stdout.write("Hello World")
        self.ingestFile()

    def ingestFile(self):
        file = open('data/products.csv', 'r')
        reader = csv.reader(file)
        for row in reader:
            print row
        file.close()
