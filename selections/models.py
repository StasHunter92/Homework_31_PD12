from django.db.models import CharField, ManyToManyField, ForeignKey, Model, CASCADE

from ads.models import Advertisement
from authentication.models import User


# ----------------------------------------------------------------------------------------------------------------------
# Create selection model
class Selection(Model):
    name: CharField = CharField(max_length=50)
    items: ManyToManyField = ManyToManyField(Advertisement, default=[])
    owner: ForeignKey = ForeignKey(User, on_delete=CASCADE)

    class Meta:
        verbose_name: str = "Подборка"
        verbose_name_plural: str = "Подборки"

    def __str__(self):
        return self.name
