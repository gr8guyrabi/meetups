from django.contrib import admin
from .models import Meetup, Location

# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    list_filter = ('name', )
    search_fields = ('name', 'address', )


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location, LocationAdmin)
