from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.my_web_site.validators import validate_only_letters


class Profile(models.Model):
    MAX_LENGTH_FIRST_NAME = 15
    MIN_LENGTH_FIRST_NAME = 2

    MAX_LENGTH_LAST_NAME = 15
    MIN_LENGTH_LAST_NAME = 2

    MIN_VALUE_BUDGET = 0.0

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_only_letters,
        )
    )

    budget = models.FloatField(
        default=0.0,
        validators=(
            MinValueValidator(MIN_VALUE_BUDGET),
        )
    )

