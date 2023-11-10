from django.contrib.gis.db import models

from .person import Person
from .uuid_model import UUIDModel


# Define the EmailAccount model
class EmailAccount(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_address = models.EmailField()
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)