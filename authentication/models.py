from datetime import date
from dateutil.parser import parse as du_parse
from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import PositiveIntegerField, ManyToManyField, CharField, TextChoices, DateField, EmailField

from locations.models import Location


# ----------------------------------------------------------------------------------------------------------------------
# Custom validators
def check_user_minimal_age(value: date):
    user_birthdate: date = value
    today_date: date = du_parse(date.today().strftime("%Y-%m-%d"))
    if relativedelta(today_date, user_birthdate).years < 9:
        raise ValidationError(f"You are too young to be registered")


# ----------------------------------------------------------------------------------------------------------------------
# Create user model
class User(AbstractUser):
    class Roles(TextChoices):
        ADMIN = "admin", "Администратор"
        MODERATOR = "moderator", "Модератор"
        MEMBER = "member", "Пользователь"

    age: PositiveIntegerField = PositiveIntegerField(null=True)
    birth_date: DateField = DateField(null=True, validators=[check_user_minimal_age])
    email: EmailField = EmailField(null=True)
    locations: ManyToManyField = ManyToManyField(Location, default=[])
    role: CharField = CharField(max_length=9, choices=Roles.choices, default=Roles.MEMBER)

    class Meta:
        verbose_name: str = "Пользователь"
        verbose_name_plural: str = "Пользователи"

        ordering: list[str] = ["username"]

    def __str__(self):
        return self.username
