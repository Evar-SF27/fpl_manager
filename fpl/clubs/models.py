from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True)
    logo_url = models.CharField(max_length=255)
    stadium = models.CharField(max_length=255)
    rivals = models.CharField(max_length=255)
    coach = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True)
    capacity = models.CharField(max_length=255, blank=True)
    ground_url = models.CharField(max_length=255)
    jersey_one = models.CharField(max_length=255, blank=True)
    jersey_two = models.CharField(max_length=255, blank=True)
    jersey_three = models.CharField(max_length=255, blank=True)
    goalkeeper = models.CharField(max_length=255, blank=True)
    sponsor_one = models.CharField(max_length=255, blank=True)
    sponsor_two = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Clubs'

    def __str__(self):
        return self.name