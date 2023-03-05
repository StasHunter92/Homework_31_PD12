from rest_framework import serializers

from ads.models import Advertisement
from ads.serializers import AdvertisementDetailSerializer
from selections.models import Selection


# ----------------------------------------------------------------------------------------------------------------------
# Selection serializers
class SelectionListSerializer(serializers.ModelSerializer):
    """
    Serializer for ListView
    """

    class Meta:
        model: Selection = Selection
        fields: list[str] = ["id", "name"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for DetailView
    """
    items: AdvertisementDetailSerializer = AdvertisementDetailSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model: Selection = Selection
        fields: str = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for CreateView
    """
    items: serializers.SlugRelatedField = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Advertisement.objects.all(),
        slug_field="id"
    )

    def is_valid(self, raise_exception=False) -> bool:
        """
        Validate data

        :return: True of False
        """
        self.initial_data["owner"] = self.context["request"].user.id
        self._items: list = self.initial_data.pop("items", [])

        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        """
        Create a new selection
        """
        selection = super().create(validated_data)

        if len(self._items) > 0:
            for item in self._items:
                selection.items.add(item)

        selection.save()

        return selection

    class Meta:
        model: Selection = Selection
        fields: str = "__all__"


class SelectionUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for UpdateView
    """
    items: serializers.SlugRelatedField = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Advertisement.objects.all(),
        slug_field="id"
    )

    def is_valid(self, raise_exception=False) -> bool:
        """
        Validate data

        :return: True of False
        """
        self.initial_data["owner"] = self.context["request"].user.id
        self._items: list = self.initial_data.pop("items", [])

        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        """
        Save changes to selection
        """
        selection = super().save()

        selection.items.set(self._items)

        selection.save()

        return selection

    class Meta:
        model: Selection = Selection
        fields: str = "__all__"


class SelectionDeleteSerializer(serializers.ModelSerializer):
    """
    Serializer for DeleteView
    """
    model: Selection = Selection
    fields: list[str] = ["id"]
