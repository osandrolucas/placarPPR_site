from django.contrib import admin
from .models import Post


class PlacarPPRadmin(admin.ModelAdmin):
    list_display = ['title', 'qt_salarios', 'published_date', 'publicador']
    search_fields = ['title']



admin.site.register(Post, PlacarPPRadmin)
