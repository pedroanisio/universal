from django.contrib.gis.db import models

from .person import Person
from .uuid_model import UUIDModel


# Define the Address model
class Address(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    ground_zero = models.PointField(blank=True)    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    # return the full address
    def __str__(self):
        return self.street + ", " + self.city + ", " + self.state + ", " + self.country + ", " + self.zip_code