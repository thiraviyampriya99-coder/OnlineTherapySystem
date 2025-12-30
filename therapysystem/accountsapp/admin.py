from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import your custom user model


# Optional: customize admin display for your CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_therapist']

    # Add your custom fields to fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_therapist',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('is_therapist',)}),
    )


# Register the CustomUser model with the customized admin
admin.site.register(CustomUser, CustomUserAdmin)
