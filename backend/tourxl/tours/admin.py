from django.contrib import admin

from tours.models import Tours


class ToursAdmin(admin.ModelAdmin):
    list_display = ("name", "duration", "price", "locations", "difficulty_level")


# Register your models here.
admin.site.register(Tours, ToursAdmin)
