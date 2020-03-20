from django import forms
from .models import Tag, Person, Location

class PhotoForm(forms.Form):
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    time_frame = forms.CharField(required=False, max_length=100)
    description = forms.CharField(max_length=1000)
    location = forms.CharField(max_length=1000)
    tags = forms.CharField(max_length=1000)
    people = forms.CharField(max_length=1000)



def get_possible_tags():
    return [tag.tag for tag in Tag.objects.all()]

def get_possible_locations():
    return [loc.location for loc in Location.objects.all()]

def get_possible_people():
    return [person.name for person in Person.objects.all()]
