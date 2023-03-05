import pytest


@pytest.mark.django_db
def test_advertisements_detail(client, advertisement, bearer_token: str):
    expected_response: dict = {
        "name": "",
        "author": "",
        "price": 100,
        "description": None,
        "is_published": False,
        "image": None,
        "category": "",
        "locations": []
    }

    response = client.get(
        f"/ad/{advertisement.pk}/",
        HTTP_AUTHORIZATION=f"Bearer {bearer_token}"
    )

    assert response.status_code == 200
    assert response.data == expected_response
