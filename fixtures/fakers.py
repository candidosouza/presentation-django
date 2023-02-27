from faker.factory import Factory as FakerFactory
from faker.generator import Generator


class Factory:
    @staticmethod
    def create() -> Generator:
        faker = FakerFactory.create()
        return faker
