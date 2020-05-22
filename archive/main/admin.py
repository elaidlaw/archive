from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(PersonInPhoto)
admin.site.register(TagsOnPhoto)
admin.site.register(PossibleDates)

class TagsInLine(admin.TabularInline):
    model = TagsOnPhoto
    extra = 0

class PersonInLine(admin.TabularInline):
    model = PersonInPhoto
    extra = 0


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("image_field", "location", "start_date", "end_date")

    inlines = [
        TagsInLine, PersonInLine
    ]
