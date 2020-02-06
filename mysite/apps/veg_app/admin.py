from django.contrib import admin
from .models import Product, Farm
from django.contrib import admin

# Register your models here.
# admin.site.register
# class FarmAdmin(admin.ModelAdmin):
#     list_display = ('name', )




admin.site.register(Product)
admin.site.register(Farm)
