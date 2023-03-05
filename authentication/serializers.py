from datetime import date
from dateutil.parser import parse as du_parse
from dateutil.relativedelta import relativedelta

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from authentication.models import User
from locations.models import Location


# ----------------------------------------------------------------------------------------------------------------------
# Custom validators
class CheckEmailDomain:
    def __init__(self, blocked_domains):
        if not isinstance(blocked_domains, list):
            blocked_domains = [blocked_domains]

        self.blocked_domains = blocked_domains

    def __call__(self, email):
        if email.split("@")[-1] in self.blocked_domains:
            raise serializers.ValidationError("Your domain is blocked")


def check_user_minimal_age(value: date):
    user_birthdate: date = value
    today_date = du_parse(date.today().strftime("%Y-%m-%d"))
    if relativedelta(today_date, user_birthdate).years < 9:
        raise serializers.ValidationError(f"Your age must be more than 9 years")


# ----------------------------------------------------------------------------------------------------------------------
# User serializers
class UserListSerializer(serializers.ModelSerializer):
    """
    Serializer for ListView
    """
    locations: serializers.SlugRelatedField = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model: User = User
        exclude: list[str] = ["password", "is_superuser", "is_staff", "is_active", "role", "groups", "user_permissions"]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for DetailView
    """
    locations: serializers.SlugRelatedField = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model: User = User
        exclude: list[str] = ["id"]


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for CreateView
    """
    age: serializers.IntegerField = serializers.IntegerField(read_only=True)
    email: serializers.EmailField = serializers.EmailField(validators=[CheckEmailDomain("rambler.ru"),
                                                                       UniqueValidator(queryset=User.objects.all())])
    locations: serializers.SlugRelatedField = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )
    role: serializers.CharField = serializers.CharField(read_only=True)

    class Meta:
        model: User = User
        fields: str = "__all__"

    def is_valid(self, raise_exception=False) -> bool:
        """
        Validate data

        :return: True of False
        """
        self._locations: list = self.initial_data.pop("locations", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        """
        Create a new user
        """
        user = super().create(validated_data)

        user.set_password(user.password)

        if len(self._locations) > 0:
            for location in self._locations:
                location_obj, _ = Location.objects.get_or_create(name=location)
                user.locations.add(location_obj)

        user_birthdate: date = du_parse(validated_data.get("birth_date"))
        today_date: date = du_parse(date.today().strftime("%Y-%m-%d"))
        user.age = relativedelta(today_date, user_birthdate).years
        user.save()

        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for UpdateView
    """
    age: serializers.IntegerField = serializers.IntegerField(read_only=True)
    birth_date: serializers.DateField = serializers.DateField(required=False, validators=[check_user_minimal_age])
    email: serializers.EmailField = serializers.EmailField(required=False,
                                                           validators=[CheckEmailDomain("rambler.ru"),
                                                                       UniqueValidator(queryset=User.objects.all())])
    id: serializers.IntegerField = serializers.IntegerField(read_only=True)
    locations: serializers.SlugRelatedField = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )
    role: serializers.CharField = serializers.CharField(read_only=True)

    class Meta:
        model: User = User
        fields: str = "__all__"

    def is_valid(self, raise_exception=False) -> bool:
        """
        Validate data

        :return: True of False
        """
        self._locations: list = self.initial_data.pop("locations", [])

        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        """
        Save changes to user
        """
        user = super().save()

        if len(self._locations) > 0:
            for location in self._locations:
                location_obj, _ = Location.objects.get_or_create(name=location)
                user.locations.add(location_obj)

        if self.initial_data.get("birth_date"):
            user_birthdate: date = du_parse(self.initial_data.get("birth_date"))
            today_date: date = du_parse(date.today().strftime("%Y-%m-%d"))
            user.age = relativedelta(today_date, user_birthdate).years

        user.save()

        return user


class UserDeleteSerializer(serializers.ModelSerializer):
    """
    Serializer for DeleteView
    """

    class Meta:
        model: User = User
        fields: list[str] = ["id"]
