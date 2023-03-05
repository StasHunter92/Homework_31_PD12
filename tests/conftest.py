from pytest_factoryboy import register

from tests.ads.factories import CategoryFactory, AdvertisementFactory, UserFactory

# ----------------------------------------------------------------------------------------------------------------------
# Register factories
register(UserFactory)
register(CategoryFactory)
register(AdvertisementFactory)

# ----------------------------------------------------------------------------------------------------------------------
# Register fixtures
pytest_plugins = "tests.fixtures"

