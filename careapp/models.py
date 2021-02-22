from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Reg_Franchise(models.Model):
    Name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(unique=True)
    Image = models.ImageField(upload_to='media', default='Nil')
    State = models.CharField(max_length=60)
    District = models.CharField(max_length=50)
    City = models.CharField(max_length=50)

    def __str__(self):
        return self.City


class franchise(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Phone = PhoneNumberField(unique=True)
    State = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    City = models.CharField(max_length=100)




