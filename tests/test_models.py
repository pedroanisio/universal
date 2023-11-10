import uuid

## tests for person model
## write all tests
from django.contrib.gis.db import models
from django.test import TestCase
from personal.models import (Address, AddressHistory, EmailAccount,
                             EmailHistory, MobileAccount, MobileHistory,
                             Person, PersonalDocument, Region)


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="John", last_name="Doe")
        Person.objects.create(first_name="Jane", last_name="Doe")

    def test_person_str(self):
        """Person str return first_name + last_name"""
        john = Person.objects.get(first_name="John")
        jane = Person.objects.get(first_name="Jane")
        self.assertEqual(john.__str__(), "John Doe")
        self.assertEqual(jane.__str__(), "Jane Doe")