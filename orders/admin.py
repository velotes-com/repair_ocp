from django.contrib import admin
from .models import Order

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["number", "status", "client_name", "client_phone", "device_model", "problem_description", "final_price"]
    list_display_links = ["number"]

admin.site.register(Order, PostAdmin)
# admin.site.register()