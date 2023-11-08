from django.contrib import admin

from users.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Класс админки для продуктов
    """
    list_display = ('first_name', 'last_name', 'email',)
    list_filter = ('first_name', 'last_name',)