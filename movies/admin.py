from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"Url": ("Name",)}


admin.site.register(Category, CategoryAdmin)


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"Url": ("Name",)}


admin.site.register(Genre, GenreAdmin)

admin.site.register(DirectorsActors)


class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"Url": ("Title",)}


admin.site.register(Movie, MovieAdmin)

admin.site.register(RatingStars)
admin.site.register(Rating)
admin.site.register(FrameOfMovies)
admin.site.register(Reviews)
