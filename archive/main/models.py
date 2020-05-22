from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=40)
    def __str__(self):
        return self.location

class Photo(models.Model):
    image_field = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.CharField(max_length=1000, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

class Person(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.tag

class PersonInPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

class TagsOnPhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.SET_NULL, null=True)
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

class PossibleDates(models.Model):
    timeframe = models.CharField(max_length=50)
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)

    def __str__(self):
        return 'Timeframe: {}'.format(self.timeframe)


# Create your models here.
