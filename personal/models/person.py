from django.contrib.gis.db import models

from .uuid_model import UUIDModel

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Non-Binary", "Non-Binary"),
    ("NotInformed", "NotInformed"),
)

# Define the Person model
class Person(UUIDModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    prefix_title = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)

    def __str__(self): 
        ## first_name and last_name are fields of your model
        return self.first_name + " " + self.last_name