from django.contrib import admin

# Import models
from collection.models import business

# Automated slug creation
class businessAdmin(admin.ModelAdmin):
    model = business
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register model
admin.site.register(business, businessAdmin)

