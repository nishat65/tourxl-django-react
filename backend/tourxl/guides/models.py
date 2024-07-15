from django.db import models

from tourxl.models import DateTimeField


# Create your models here.
class Guides(DateTimeField):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    office_address = models.TextField(null=True, blank=True)
    total_tours_done = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "guides"
        verbose_name_plural = "Guides"
        ordering = ["-total_tours_done"]
        indexes = [
            models.Index(fields=["phone"], name="phone_idx"),
            models.Index(fields=["email"], name="email_idx"),
        ]
