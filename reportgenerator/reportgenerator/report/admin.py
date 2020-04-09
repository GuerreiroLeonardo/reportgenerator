from django.contrib import admin
from .models import Market

class CreatePageAdmin(admin.ModelAdmin):

    list_display = ['market_name', 'created_at']
    search_fields = ['market_name', 'created_at']

admin.site.register(Market)


