from .models import User, Product, Order
from django.contrib import admin


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)

class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registered_at']
    ordering = ['name']
    list_filter = ['address', 'registered_at']
    search_fields = ['name']
    search_help_text = 'Поиск имени по полю (name)'

    """Отдельный продукт."""
    # fields = ['name', 'email', 'phone', 'address']
    readonly_fields = ['address']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Электронный адрес и телефон:',
                        'fields':['email', 'phone'],
        },
        ),
        (
            'Адрес:',
            {
                'fields': ['address'],
            }
        )
    ]

class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['title', 'description', 'price', 'count', 'added_at']
    ordering = ['price', '-count']
    list_filter = ['price', 'added_at']
    search_fields = ['title']
    search_help_text = 'Поиск по полю (title)'
    actions = [reset_quantity]



class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'ordered_at']
    list_filter = ['ordered_at']






admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)