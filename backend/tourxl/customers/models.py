from django.db import models

from tourxl.models import DateTimeField


# Create your models here.
class Customers(DateTimeField):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "customers"
        verbose_name_plural = "Customers"
        indexes = [
            models.Index(fields=["phone"], name="cus_phone_idx"),
            models.Index(fields=["email"], name="cus_email_idx"),
        ]
