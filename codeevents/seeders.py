from fixtures.seeder import Seeder


class DatabaseSeeder:
    @classmethod
    def run(cls):
        MarathonSeeder.run()


class MarathonSeeder(Seeder):
    @classmethod
    def run(cls):
        cls.load_fixtures('user.json', 'events')
        cls.load_fixtures('landingpages.json', 'events')
        cls.load_fixtures('events.json', 'events')
        cls.load_fixtures('user_registration.json', 'events')
