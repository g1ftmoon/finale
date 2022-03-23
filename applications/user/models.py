from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='users.photo', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_name

