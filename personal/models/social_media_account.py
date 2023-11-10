from django.contrib.gis.db import models

from .person import Person
from .uuid_model import UUIDModel

PLATFORM_NAME_CHOICES = (
    ("Facebook", "Facebook"),
    ("Twitter", "Twitter"),
    ("Instagram", "Instagram"),
)

# Define the SocialMediaAccount model
class SocialMediaAccount(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=255, choices=PLATFORM_NAME_CHOICES)
    username = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)