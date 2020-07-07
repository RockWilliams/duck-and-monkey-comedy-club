from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
def validate_email(value):
    if "." in value:
        return value
    else: 
        return ValidationError('Email Must Include at least one "." ')

class Subscriber(models.Model):
    alnum = RegexValidator(r'^[a-z,A-Z]*$', 'Name Must Only Contain Letters')
    first_name = models.CharField(max_length=100,validators=[alnum,MinLengthValidator(2)])
    last_name = models.CharField(max_length=100,validators=[alnum,MinLengthValidator(2)])
    email = models.EmailField(max_length=200, validators=[validate_email])
    REQUIRED = ["first_name","last_name","email"]

    def full_name(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def __str__(self):
        return f"{self.first_name}"

