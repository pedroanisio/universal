from django.contrib.gis.db import models

from .mobile_account import MobileAccount
from .person import Person
from .uuid_model import UUIDModel


# Define the MobileHistory model
class MobileHistory(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    mobile_id = models.ForeignKey(MobileAccount, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)