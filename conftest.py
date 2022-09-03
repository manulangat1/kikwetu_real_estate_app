import pytest 
from pytest_factoryboy import register 

from tests.factories import UserFactory, ProfileFactory

register(ProfileFactory)
register(UserFactory)

@pytest.fixture
def base_user(db, user_factory):
    new_user = user_factory.create()
    return new_user
@pytest.fixture
def create_super_user(db, user_factory):
    new_user = user_factory.create(is_staff=True,is_superuser=True)
    return new_user
@pytest.fixture
def profile(db, profile_factory):
    new_profile = profile_factory.create()
    return new_profile