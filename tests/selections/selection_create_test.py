import pytest


@pytest.mark.django_db
def test_create_selection(client, bearer_token: str):
    expected_response: dict = {
        "id": 1,
        "items": [],
        "name": "TestMemberSelection",
        "owner": 8
    }

    data: dict = {"name": "TestMemberSelection"}

    response = client.post(
        "/selection/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {bearer_token}"
    )

    assert response.status_code == 201
    assert response.data == expected_response
