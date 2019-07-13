from django.db import models


class PhoneBook(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name
