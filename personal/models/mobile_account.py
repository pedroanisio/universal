from django.contrib.gis.db import models

from .person import Person
from .uuid_model import UUIDModel


# Define the MobileAccount model
class MobileAccount(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)