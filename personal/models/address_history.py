from django.contrib.gis.db import models

from .uuid_model import UUIDModel
from .person import Person 
from .address import Address

# Define the AddressHistory model
class AddressHistory(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)