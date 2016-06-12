from django.contrib import admin

# Import models
from collection.models import Business

# Automated slug creation
class BusinessAdmin(admin.ModelAdmin):
    model = Business
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register model
admin.site.register(Business, BusinessAdmin)

