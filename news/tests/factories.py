import random

import factory

from faker import Faker
from factory.django import DjangoModelFactory

from news.models import Author, Notice

fake = Faker('pt_BR')


class AuthorFactory(DjangoModelFactory):

    class Meta:
        model = Author

    id = random.randint(1000, 99999)
    name = fake.name()


class NoticeFactory(DjangoModelFactory):

    class Meta:
        model = Notice

    id = random.randint(1000, 99999)
    title = fake.name()
    notice = fake.name()
    author = factory.SubFactory(AuthorFactory)
