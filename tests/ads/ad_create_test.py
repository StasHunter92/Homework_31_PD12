import pytest

from ads.models import Category


@pytest.mark.django_db
def test_advertisements_create(client, bearer_token: str):
    category: Category = Category.objects.create(name="testname", slug="testslug")

    expected_response: dict = {
        "id": 1,
        "name": "TestCreateAdvertisement",
        "author": 1,
        "price": 10,
        "description": None,
        "is_published": False,
        "image": None,
        "category": category.id,
    }

    data: dict = {
        "name": "TestCreateAdvertisement",
        "category": 1,
        "price": 10,
        "is_published": False
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {bearer_token}"
    )

    assert response.status_code == 201
    assert response.data == expected_response
