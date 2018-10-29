from django.contrib import admin
from movies.models import Movie,Actor,Acted

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Acted)

