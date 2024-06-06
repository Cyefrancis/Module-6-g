from django.contrib import admin
from .models import Users
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","age","email","phone_number")

admin.site.register(Users, UsersAdmin)