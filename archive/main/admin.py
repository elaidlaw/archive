from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Photo)
admin.site.register(PersonInPhoto)
admin.site.register(TagsOnPhoto)
admin.site.register(PossibleDates)
