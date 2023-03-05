import pytest


# ----------------------------------------------------------------------------------------------------------------------
# Create fixtures
@pytest.fixture
@pytest.mark.django_db
def bearer_token(client, django_user_model) -> str:
    """
    Get the access token for testing

    :return: String access token
    """
    username: str = "TestMember"
    password: str = "TestMember"

    django_user_model.objects.create_user(username=username, password=password)

    response = client.post(
        "/user/token/",
        {
            "username": username,
            "password": password,
        },
        format="json"
    )

    return response.data.get("access")
