from django.contrib import admin

from bookings.models import Bookings


class BookingsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "tour_date",
        "booking_date",
        "number_of_people",
        "total_price",
        "status",
    )


admin.site.register(Bookings, BookingsAdmin)
