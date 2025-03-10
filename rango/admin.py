from django.contrib import admin
from unicodedata import category

from rango.models import Category, Page

# Register your models here.
admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

admin.site.register(Page, PageAdmin)
