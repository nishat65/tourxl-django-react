from django.contrib import admin
from customers.models import Customers


# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email", "password", "address")


admin.site.register(Customers, CustomersAdmin)
