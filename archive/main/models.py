from django.db import models

class Photo(model.Models):
    image_field = models.CharField(max_length=30)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    description = models.CharField(max_length=1000)

class Person(model.Models):
    name = models.CharField(max_length=40)

class Location(model.Models):
    location = models.CharField(max_length=20)

class Tag(model.Models):
    tag = models.CharField(max_length=40)

class PersonInPhoto(model.Models):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL)

class LocationOfPhoto(model.Models):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL)

class TagsOnPhoto(model.Models):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL)



# Create your models here.
