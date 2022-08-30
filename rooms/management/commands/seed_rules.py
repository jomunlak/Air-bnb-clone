from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates house rules"

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        numbers = options.get("numbers")
        for i in range(numbers):
            room_models.HouseRule.objects.create(name=seeder.faker.word())

        self.stdout.write(self.style.SUCCESS(f"{numbers} rules created"))

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers", default=1, type=int, help="How many rules do you want"
        )
