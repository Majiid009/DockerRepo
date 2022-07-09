from django.contrib import admin
from .models import CustomUser
# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']

admin.site.register(CustomUser, UsersAdmin)

