from django.db import models
from Users.models import UserProfile
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(UserProfile):
    phone_number= PhoneNumberField(verbose_name="Phone number of Customers")    
    date_in = models.DateTimeField(auto_now=True)
    date_out = models.DateTimeField(auto_now= False, blank = True, null = True)
    