from django.core.management.base import BaseCommand, CommandParser
from dashboard.models import Client
from faker import Faker
import random

class DataSeeder:
    def __init__(self, model_class):
        self.model_class = model_class
        self.fake = Faker()

    def create_fake_record(self):
        return self.model_class.objects.create(
            name=self.fake.name(),
            age=random.randint(18, 65),
            city=self.fake.city(),
            salary=round(random.uniform(50000, 150000), 2)
        )

class Command(BaseCommand):
    help = 'Seeds database with fake data'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('model', type=str, help='Model to seed')
        parser.add_argument('count', type=int, help='Number of records to create')

    def handle(self, *args, **kwargs) -> str | None:
        model_name = kwargs['model']
        count = kwargs['count']

        self.stdout.write(f'Seeding {count} {model_name} records')

        seeder = None

        if model_name.lower() == 'client':
            seeder = DataSeeder(Client)

        if seeder:
            for _ in range(count):
                seeder.create_fake_record()
            self.stdout.write(f'{count} {model_name} records created successfully')
        else:
            self.stdout.write('Model not found')
