from django.db import models
from django.utils import timezone


class Ad(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    wherefrom = models.CharField(max_length=150)
    whereto = models.CharField(max_length=150)
    when = models.DateTimeField(auto_now=False, auto_now_add=False)
    photo = models.ImageField(blank=True)
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='ads')
    date_pub = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_pub']


class AdDriver(Ad, models.Model):
    active = models.BooleanField(blank=False)
    car_photo = models.ImageField(blank=True)
    car_info = models.TextField(blank=True)
    history = models.CharField(max_length=255)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)
