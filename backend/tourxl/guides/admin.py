from django.contrib import admin

from guides.models import Guides


# Register your models here.
class GuidesAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone",
        "email",
        "password",
        "office_address",
        "total_tours_done",
    )

    ordering = ["-total_tours_done"]


admin.site.register(Guides, GuidesAdmin)
