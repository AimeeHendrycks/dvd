from django.db import models


class Genre(models.Model):
    genre =models.CharField(max_length=500, null=True, blank=True)

class Studio(models.Model):
    studio = models.CharField(max_length=500, null=True, blank=True)

class Dvd(models.Model):
    title= models.CharField(max_length=500, null=True, blank=True)
    studio = models.ForeignKey('main.Studio', null=True, blank=True)
    released = models.CharField(max_length=500, null=True, blank=True)   
    status =models.CharField(max_length=500, null=True, blank=True)
    sound =models.CharField(max_length=500, null=True, blank=True)
    versions =models.CharField(max_length=500, null=True, blank=True)
    price =models.CharField(max_length=500, null=True, blank=True)
    rating =models.CharField(max_length=500, null=True, blank=True)
    year =models.CharField(max_length=500, null=True, blank=True)
    genre =models.ForeignKey('main.Genre', null=True, blank=True)
    aspect =models.CharField(max_length=500, null=True, blank=True)
    upc =models.CharField(max_length=500, null=True, blank=True)
    dvd_release_date =models.CharField(max_length=500, null=True, blank=True)
    dvd_id =models.IntegerField(null=True, blank=True)
    timestamp =models.CharField(max_length=500, null=True, blank=True)

    def __unidecode__(self):
        return '%s' % self.title
