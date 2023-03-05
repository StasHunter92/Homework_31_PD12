from django.core.validators import MinValueValidator, MinLengthValidator
from django.db.models import CharField, ForeignKey, BooleanField, ImageField, Model, CASCADE, IntegerField

from authentication.models import User


# ----------------------------------------------------------------------------------------------------------------------
# Create category model
class Category(Model):
    name: CharField = CharField(max_length=30)
    slug: CharField = CharField(null=True, max_length=10, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name: str = "Категория"
        verbose_name_plural: str = "Категории"

        ordering: list[str] = ["name"]

    def __str__(self):
        return self.name


# ----------------------------------------------------------------------------------------------------------------------
# Create advertisement model
class Advertisement(Model):
    PUBLISHED: list[tuple] = [
        (True, "Опубликовано"),
        (False, "Не опубликовано")
    ]

    author: ForeignKey = ForeignKey(User, on_delete=CASCADE)
    category: ForeignKey = ForeignKey(Category, on_delete=CASCADE)
    description: CharField = CharField(max_length=500, null=True)
    image: ImageField = ImageField(upload_to="images/", null=True)
    is_published: BooleanField = BooleanField(choices=PUBLISHED, default=False)
    name: CharField = CharField(max_length=60, null=False, validators=[MinLengthValidator(10)])
    price: IntegerField = IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name: str = "Объявление"
        verbose_name_plural: str = "Объявления"

        ordering: list[str] = ["-price"]

    def __str__(self):
        return self.name
