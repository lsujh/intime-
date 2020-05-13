from django.contrib import admin
from .models import AppleId

@admin.register(AppleId)
class AppleIdAdmin(admin.ModelAdmin):
    model = AppleId

