from django.core.management.base import BaseCommand

from mortgage.models import BankModel

class Command(BaseCommand):
    help = 'Populate some db data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Begin populating db'))

        for i in range(10):
            BankModel.objects.create(bank_name=f'bank_{i+1}')

        self.stdout.write(self.style.SUCCESS('Done populating db'))