from django.db import models
from django.contrib.gis.db import models
import uuid

# Define choices for the document_type and platform_name fields
DOCUMENT_TYPE_CHOICES = (
    ("Passport", "Passport"),
    ("CPF", "CPF"),
    ("RG", "RG"),
    ("DriverLicense", "DriverLicense"),
    ("RNE", "RNE"),
    ("SocialSec", "SocialSec")   
)

PLATFORM_NAME_CHOICES = (
    ("Facebook", "Facebook"),
    ("Twitter", "Twitter"),
    ("Instagram", "Instagram"),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Non-Binary", "Non-Binary"),
    ("NotInformed", "NotInformed"),
)

class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

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

# Define the Region model
class Region(UUIDModel):
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    area = models.PolygonField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

# Define the AddressHistory model
class AddressHistory(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the EmailAccount model
class EmailAccount(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_address = models.EmailField()
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the EmailHistory model
class EmailHistory(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_id = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the MobileAccount model
class MobileAccount(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the MobileHistory model
class MobileHistory(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    mobile_id = models.ForeignKey(MobileAccount, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the PersonalDocument model
class PersonalDocument(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=255, choices=DOCUMENT_TYPE_CHOICES)
    document_number = models.CharField(max_length=255)
    issuer_authority = models.CharField(max_length=255,blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

# Define the SocialMediaAccount model
class SocialMediaAccount(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=255, choices=PLATFORM_NAME_CHOICES)
    username = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
