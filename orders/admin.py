from django.contrib import admin
from .models import Order

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("str_number_order", "status", "priority", "client_name", "client_phone", "device_model", "problem_description",
                    "final_price")
    list_display_links = ("str_number_order", )
    list_editable = ("priority", )
    readonly_fields = ("watch_count", )
    list_filter = ("status", "priority", )

    def str_number_order(self, obj):
        return f"Заказ № {obj.number_order:04d}"

    str_number_order.short_description = "Номер заказа"  # Заголовок колонки
    str_number_order.admin_order_field = 'number_order'  # Для возможности сортировки

# admin.site.register(Order)
admin.site.register(Order, PostAdmin)