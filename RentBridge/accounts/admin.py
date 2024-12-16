from django.contrib import admin
from .models import CustomUser


class CustomAdmin(admin.ModelAdmin):
    """ Customizing the admin view for the CustomUser model """
    list_display = [
        'email', 'firstname',
        'lastname', 'is_verified', 'is_active', 'is_staff']

admin.site.register(CustomUser, CustomAdmin)
