from django.contrib import admin

from ratings.models import Ratings


class RatingsAdmin(admin.ModelAdmin):
    list_display = ("customer", "guide", "rating")


admin.site.register(Ratings, RatingsAdmin)
