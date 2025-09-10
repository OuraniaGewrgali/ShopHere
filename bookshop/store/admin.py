from django.contrib import admin
from .models import Category, Book

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "price", "stock", "featured", "created_at")
    list_filter = ("category", "featured")
