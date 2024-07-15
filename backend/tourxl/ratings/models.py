from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from tourxl.models import DateTimeField

"""
CREATE TABLE ratings (
    id SERIAL PRIMARY KEY,
    customerid INTEGER REFERENCES customers(id),
    guideid INTEGER REFERENCES guides(id),
    rating INTEGER NOT NULL CHECK (
        rating BETWEEN 1 AND 5
    ),
    createdAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
"""


# Create your models here.
class Ratings(DateTimeField):
    customer = models.ForeignKey("customers.Customers", on_delete=models.CASCADE)
    guide = models.ForeignKey("guides.Guides", on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.rating}"

    class Meta:
        db_table = "ratings"
        verbose_name_plural = "Ratings"
