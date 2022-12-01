from django.contrib import admin
from .models import Movie
# Register your models here.ư
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Movie, MovieAdmin)
