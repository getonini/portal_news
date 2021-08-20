import pytest
from django.conf import settings
from django.contrib.auth.models import User
from pytest_factoryboy import register

from news.tests.factories import AuthorFactory, NoticeFactory

register(AuthorFactory)
register(NoticeFactory)


@pytest.fixture
def admin_user():
    return User.objects.create(**{'username': 'admin', 'is_superuser': True})


@pytest.fixture
def customer_client(db, admin_user):
    """A Django test client logged in as an customer user."""
    return _create_client()


def _create_client():
    from django.test.client import Client
    settings.TIME_ZONE = 'UTC'
    return Client()
