from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class PersonAPITest(APITestCase):
    def test_create_person(self):
        """
        Ensure we can create a new person object.
        """
        url = reverse('person-list')
        data = {'first_name': 'John', 'last_name': ' Doe', 'gender': 'Male'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
