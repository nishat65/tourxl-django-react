from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from tourxl.models import DateTimeField


# Create your models here.
class Tours(DateTimeField):
    LEVELS = (
        ("easy", "easy"),
        ("moderate", "moderate"),
        ("challenging", "challenging"),
        ("extreme", "extreme"),
    )
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(30)],
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    locations = models.JSONField(null=True, blank=True)
    max_participants = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(30)],
    )
    difficulty_level = models.CharField(
        choices=LEVELS, null=False, blank=False, max_length=100
    )
    language = models.CharField(max_length=100, null=True, blank=True)
    included = ArrayField(
        models.CharField(max_length=100), null=True, blank=True, size=100
    )
    not_included = ArrayField(
        models.CharField(max_length=100), null=True, blank=True, size=100
    )
    meeting_point = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "tours"
        verbose_name_plural = "Tours"
        ordering = ["-duration"]
