from django.contrib import admin
from .models import TherapistAvailability, Session

# Register your models here.

admin.site.register(TherapistAvailability)
admin.site.register(Session)