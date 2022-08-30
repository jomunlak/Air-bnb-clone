import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates reviews"

    def handle(self, *args, **options):
        number = options.get("numbers", 1)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(1, 6),
                "communication": lambda x: random.randint(1, 6),
                "cleanliness": lambda x: random.randint(1, 6),
                "location": lambda x: random.randint(1, 6),
                "check_in": lambda x: random.randint(1, 6),
                "value": lambda x: random.randint(1, 6),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )

        created_reviews = seeder.execute()
        clean_reviews_id = created_reviews[review_models.Review]

        print(clean_reviews_id)

        self.stdout.write(self.style.SUCCESS(f"{number} reviews created"))

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers",
            type=int,
            default=1,
            help="How many users do you want to create",
        )
