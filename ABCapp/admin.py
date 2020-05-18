from django.contrib import admin
from ABCapp.models import Customers

class AdminCustomers(admin.ModelAdmin):
    list_display = ['name','email','mobile','created_date']



admin.site.register(Customers,AdminCustomers)

