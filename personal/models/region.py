from django.contrib.gis.db import models

from .address import Address
from .uuid_model import UUIDModel


# Define the Region model
class Region(UUIDModel):
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    area = models.PolygonField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)