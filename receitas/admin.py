from django.contrib import admin

from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'category', 'is_active']
  list_display_links = ['name']
  search_fields = ['name']
  list_filter = ['category']
  list_editable = ['is_active']
  list_per_page = 5
