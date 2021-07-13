from django.core.management.base import BaseCommand

from faker import Faker # noqa

from teachers.models import Teachers


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help='create new faker teachers')

    def handle(self, *args, **options):
        qty = options['qty']
        return Teachers.generate_teachers(qty)
