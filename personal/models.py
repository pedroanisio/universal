from django.db import models
from django.contrib.gis.db import models

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

# Define the Person model
class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    prefix_title = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)

# Define the Address model
class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    ground_zero = models.PointField()    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the Region model
class Region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    area = models.PolygonField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

# Define the AddressHistory model
class AddressHistory(models.Model):
    address_history_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the EmailAccount model
class EmailAccount(models.Model):
    email_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_address = models.EmailField()
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the EmailHistory model
class EmailHistory(models.Model):
    email_history_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_id = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the MobileAccount model
class MobileAccount(models.Model):
    mobile_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the MobileHistory model
class MobileHistory(models.Model):
    mobile_history_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    mobile_id = models.ForeignKey(MobileAccount, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

# Define the PersonalDocument model
class PersonalDocument(models.Model):
    document_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=255, choices=DOCUMENT_TYPE_CHOICES)
    document_number = models.CharField(max_length=255)
    issuer_authority = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField()

# Define the SocialMediaAccount model
class SocialMediaAccount(models.Model):
    social_media_id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=255, choices=PLATFORM_NAME_CHOICES)
    username = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
