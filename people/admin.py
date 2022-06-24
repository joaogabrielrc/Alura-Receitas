from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 5
