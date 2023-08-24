from django.db import models

# Create your models here.
class UserDetails(models.Models):
    favourite_club = models.CharField(max_length=50, blank=False)
    fpl_email = models.CharField(max_length=25, blank=False)
    fpl_password = models.CharField(max_length=25, blank=False)
    pay_number = models.CharField(max_length=15, blank=False)
    user_id = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.fpl_email
    