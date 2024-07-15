from django.db import models

from tourxl.models import DateTimeField

"""
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    guide_id INTEGER NOT NULL REFERENCES guides(id),
    tour_id INTEGER NOT NULL REFERENCES tours(id),
    booking_date DATE NOT NULL DEFAULT CURRENT_DATE,
    tour_date DATE NOT NULL,
    number_of_people INTEGER NOT NULL CHECK (number_of_people > 0),
    total_price DECIMAL(10, 2) NOT NULL CHECK (total_price >= 0),
    status VARCHAR(20) NOT NULL CHECK (
        status IN ('pending', 'confirmed', 'cancelled', 'completed')
    ),
    special_requests TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
"""


class Bookings(DateTimeField):
    STATUS = (
        ("pending", "pending"),
        ("confirmed", "confirmed"),
        ("cancelled", "cancelled"),
        ("completed", "completed"),
    )
    customer_id = models.ForeignKey(
        "customers.Customers", on_delete=models.CASCADE, related_name="customers"
    )
    guide_id = models.ForeignKey(
        "guides.Guides", on_delete=models.CASCADE, related_name="guides"
    )
    tour_id = models.ForeignKey(
        "tours.Tours", on_delete=models.CASCADE, related_name="tours"
    )
    booking_date = models.DateField()
    tour_date = models.DateField()
    number_of_people = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=STATUS, max_length=20)
    special_requests = models.TextField()

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        db_table = "bookings"
        verbose_name_plural = "Bookings"
        ordering = ["-tour_date"]
        indexes = [
            models.Index(fields=["tour_date"], name="tour_date_idx"),
            models.Index(fields=["booking_date"], name="booking_date_idx"),
        ]
