from django.contrib import admin
from .models import Category,Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}

