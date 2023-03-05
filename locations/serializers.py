from rest_framework import serializers

from locations.models import Location


# ----------------------------------------------------------------------------------------------------------------------
# Location serializers
class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for ViewSet
    """
    class Meta:
        model: Location = Location
        fields: str = "__all__"
