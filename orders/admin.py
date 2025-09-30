from django.contrib import admin
from .models import Order

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["formatted_number", "status", "client_name", "client_phone", "device_model", "problem_description",
                    "final_price"]
    list_display_links = ["formatted_number"]

    def formatted_number(self, obj):
        return f"Заказ № {obj.number:04d}"

    formatted_number.short_description = "Номер заказа"  # Заголовок колонки
    formatted_number.admin_order_field = 'number'  # Для возможности сортировки

# admin.site.register(Order)
admin.site.register(Order, PostAdmin)