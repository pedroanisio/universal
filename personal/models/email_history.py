from django.contrib.gis.db import models

from .email_account import EmailAccount
from .person import Person
from .uuid_model import UUIDModel


# Define the EmailHistory model
class EmailHistory(UUIDModel):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_id = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)