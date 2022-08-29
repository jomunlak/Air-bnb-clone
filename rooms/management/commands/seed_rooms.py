import random
from re import M
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates rooms"

    def handle(self, *args, **options):
        number = int(options.get("numbers"))
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "max_guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers", default="1", help="How many users do you want to create"
        )
