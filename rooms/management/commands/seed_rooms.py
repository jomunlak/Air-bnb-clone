import random
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
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

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

        created_rooms = seeder.execute()
        created_rooms_id = created_rooms[room_models.Room]

        for id in created_rooms_id:
            room = room_models.Room.objects.get(id=id)
            for i in range(3, random.randint(10, 25)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"/room_photo/{random.randint(1,31)}.webp",
                    room=room,
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number % 2:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number % 2:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number % 2:
                    room.house_rules.add(r)

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))

    def add_arguments(self, parser):
        parser.add_argument(
            "--numbers", default="1", help="How many rooms do you want to create"
        )
