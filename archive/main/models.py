from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=40)

class Photo(models.Model):
    image_field = models.CharField(max_length=100)
    start_date = models.DateField('start date', null=True)
    end_date = models.DateField('end date', null=True)
    description = models.CharField(max_length=1000, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

class Person(models.Model):
    name = models.CharField(max_length=40)

class Tag(models.Model):
    tag = models.CharField(max_length=40)

class PersonInPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

class TagsOnPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

class PossibleDates(models.Model):
    timeframe = models.CharField(max_length=50)
    startdate = models.DateField('start date', null=True)
    enddate = models.DateField('end date', null=True)


# Create your models here.
