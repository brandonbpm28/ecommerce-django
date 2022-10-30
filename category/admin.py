from django.contrib import admin
from .models import category

# Register your models here.

class categoryadmin(admin.ModelAdmin):
    list_display=('category_name', 'slug')
    prepopulated_fields={'slug':('category_name',)}



admin.site.register(category, categoryadmin)
