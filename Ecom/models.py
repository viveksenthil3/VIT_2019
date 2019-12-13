from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid



class customer_data(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=32)
    name = models.CharField(max_length=50)
    phone = PhoneNumberField()
    location = models.CharField(max_length=100)

