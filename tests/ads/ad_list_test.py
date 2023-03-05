import pytest

from ads.serializers import AdvertisementListSerializer
from tests.ads.factories import AdvertisementFactory


@pytest.mark.django_db
def test_advertisements_list(client, bearer_token: str):
    advertisements = AdvertisementFactory.create_batch(3)
    expected_response: dict = {
        "count": 3,
        "next": None,
        "previous": None,
        "results": AdvertisementListSerializer(advertisements, many=True).data
    }

    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == expected_response
