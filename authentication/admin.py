from django.contrib import admin

from .models import Customer

# Register your models here.


@admin.register(Customer)
class UserModelAdmin(admin.ModelAdmin):

    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff',
                    'is_superuser', 'date_joined', 'last_login', 'phone_number']
