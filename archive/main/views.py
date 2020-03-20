from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import os
import config
import json
import random

from .models import *
from .forms import *

# Create your views here.

photos_list = os.listdir(os.path.join(config.ARCHIVE_PATH, 'photos'))
for photo in photos_list:
    if len(Photo.objects.filter(image_field=photo)) > 0:
        photos_list.remove(photo)

def index(request):
    return render(request, 'main/index.html', { 'list': photos_list })

def new_image_to_annotate(request):
    print(len(photos_list))
    photo = random.choice(photos_list)
    photos_list.remove(photo)
    print(len(photos_list))
    print(photos_list)

    return HttpResponseRedirect(reverse('input-img', args=[photo]))

def input(request, img):
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            start_date = data['start_date']
            print(start_date)
            end_date = data['end_date']
            if start_date != None:
                if end_date == None:
                    end_date = start_date
            else:
                if len(PossibleDates.objects.filter(timeframe=data['timeframe'])):
                    timeframe = PossibleDates.objects.get(timeframe=data['timeframe'])
                    start_date = timeframe.startdate
                    end_date = timeframe.enddate
            location = data['location']
            if len(Location.objects.filter(location=location)) == 0:
                Location.objects.create(location=location)
            location = Location.objects.get(location=location)
            photo = Photo.objects.create(
                image_field=img,
                location=location,
                start_date=start_date,
                end_date=end_date,
                description=data['description'],
            )

            tags = json.loads(data['tags'])
            for tag in tags:
                if len(Tag.objects.filter(tag=tag)) == 0:
                    Tag.objects.create(tag=tag)
                TagsOnPhoto.objects.create(tags=Tag.objects.get(tag=tag), photo=photo)
            people = json.loads(data['people'])
            for person in people:
                if len(Person.objects.filter(name=person)) == 0:
                    Person.objects.create(name=person)
                PersonInPhoto.objects.create(person=Person.objects.get(name=person), photo=photo)
        return HttpResponseRedirect(reverse('input'))


    else:
        form = PhotoForm()
        tags = get_possible_tags()
        people = get_possible_people()
        locations = get_possible_locations()

    return render(request, 'main/input.html', {'form': form, 'img': img, 'tags': json.dumps(tags), 'people': json.dumps(people), 'locations': json.dumps(locations)})
