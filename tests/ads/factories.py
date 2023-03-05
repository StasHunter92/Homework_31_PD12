import factory.django

from authentication.models import User
from ads.models import Advertisement, Category


# ----------------------------------------------------------------------------------------------------------------------
# Create factories
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category


class AdvertisementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    price: int = 100
