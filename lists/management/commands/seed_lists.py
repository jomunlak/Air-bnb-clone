import random
from secrets import choice
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models
from lists import models as list_models

NAME = "lists"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def handle(self, *args, **options):
        number = options.get("numbers", 1)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created = seeder.execute()
        cleaned = created[list_models.List]

        for id in cleaned:
            list_obj = list_models.List.objects.get(id=id)
            mid = len(rooms) // 2
            to_all = rooms[random.randint(0, mid) : random.randint(mid + 1, len(rooms))]
            list_obj.rooms.add(*to_all)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers",
            type=int,
            default=1,
            help=f"How many {NAME} do you want to create",
        )
