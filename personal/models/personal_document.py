from django.contrib.gis.db import models

from .person import Person
from .uuid_model import UUIDModel

# Define choices for the document_type and platform_name fields
DOCUMENT_TYPE_CHOICES = (
    ("Passport", "Passport"),
    ("CPF", "CPF"),
    ("RG", "RG"),
    ("DriverLicense", "DriverLicense"),
    ("RNE", "RNE"),
    ("SocialSec", "SocialSec")   
)

# Define the PersonalDocument model
class PersonalDocument(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=255, choices=DOCUMENT_TYPE_CHOICES)
    document_number = models.CharField(max_length=255)
    issuer_authority = models.CharField(max_length=255,blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)