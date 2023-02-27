from django.core.management import call_command
from fixtures.services import Seed
from faker import Factory, Faker


class Seeder:
    @classmethod
    def load_fixtures(cls, json_file, app):
        args = [
            json_file,
            '--app', app,
        ]
        call_command('loaddata', *args)

    @classmethod
    def factory(cls):
        Seed.seeders = {}
        return Seed().seeder()

    @classmethod
    def faker(cls) -> Faker:
        return Factory.create()
