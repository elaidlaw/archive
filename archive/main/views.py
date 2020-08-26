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

# photos_list = os.listdir(os.path.join(config.ARCHIVE_PATH, 'photos'))
# for photo in photos_list:
#     if len(Photo.objects.filter(image_field=photo)) > 0 or photo[0] == '.':
#         photos_list.remove(photo)

def index(request):
    return render(request, 'main/index.html', {})

def new_image_to_annotate(request):
    photo = random.choice(Photo.objects.filter(status="not done"))
    photo.status = "in progress"
    photo.save()

    return HttpResponseRedirect(reverse('input-img', args=[photo.image_field]))

def tags_list(request):
    tags = Tag.objects.all()
    tags = [(tag.tag, len(TagsOnPhoto.objects.filter(tags=tag))) for tag in tags]
    return render(request, 'main/tags_list.html', {'tags': tags})

def photos_by_tag(request, tag):
    tag = Tag.objects.get(tag=tag)
    images = [photo.photo.image_field for photo in TagsOnPhoto.objects.filter(tags=tag)]

    return render(request, 'main/photos_by_tag.html', {'tag': tag, 'images': images})

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            photo_results = []
            tag_results = {}
            for token in data['search'].split():
                photos = Photo.objects.filter(description__contains=token)
                for photo in photos:
                    photo_results.append(photo)
                tags = Tag.objects.filter(tag__contains=token)
                for tag in tags:
                    photos = [photo.photo for photo in TagsOnPhoto.objects.filter(tags=tag)]
                    tag_results[tag.tag] = photos

            return render(request, 'main/search.html', {'photo_results': photos, 'tag_results': tag_results, 'form': form})



    else:
        form = SearchForm()

        return render(request, 'main/search.html', {'photo_results': [], 'tag_results': {}, 'form': form})


def input(request, img):
    print('hello')
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            start_date = data['start_date']
            end_date = data['end_date']
            if start_date != None:
                if end_date == None:
                    end_date = start_date
            else:
                if len(PossibleDates.objects.filter(timeframe=data['time_frame'])):
                    timeframe = PossibleDates.objects.get(timeframe=data['time_frame'])
                    start_date = timeframe.startdate
                    end_date = timeframe.enddate
            location = data['location']
            if len(Location.objects.filter(location=location)) == 0:
                Location.objects.create(location=location)
            location = Location.objects.get(location=location)
            photo = Photo.objects.get(image_field=img)
            photo.status = "done"
            photo.location = location
            photo.start_date = start_date
            photo.end_date = end_date
            photo.screenshot = data['screenshot']
            photo.original = data['original']
            photo.description = data['description']
            
            photo.save()

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
            print(photo.start_date)
            print(Photo.objects.get(image_field=img).start_date)
        return HttpResponseRedirect(reverse('input'))


    else:
        form = PhotoForm()
        tags = get_possible_tags()
        people = get_possible_people()
        locations = get_possible_locations()
        time_frames = get_possible_time_frames()

    return render(request, 'main/input.html', {'form': form, 'img': img, 'tags': json.dumps(tags), 'people': json.dumps(people), 'locations': json.dumps(locations), 'time_frames': json.dumps(time_frames)})
