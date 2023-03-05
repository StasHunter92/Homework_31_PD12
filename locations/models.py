from django.db.models import CharField, DecimalField, Model


# ----------------------------------------------------------------------------------------------------------------------
# Create location model
class Location(Model):
    name: CharField = CharField(max_length=100)
    lat: DecimalField = DecimalField(max_digits=8, decimal_places=6, null=True)
    lng: DecimalField = DecimalField(max_digits=9, decimal_places=6, null=True)

    class Meta:
        verbose_name: str = "Локация"
        verbose_name_plural: str = "Локации"

        ordering: list[str] = ["name"]

    def __str__(self):
        return self.name
