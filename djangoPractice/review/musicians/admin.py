from django.contrib import admin
from .models import Album
# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'cover_img', 'musician')
admin.site.register(Album, AlbumAdmin)