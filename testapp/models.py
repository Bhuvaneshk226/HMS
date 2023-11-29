from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
