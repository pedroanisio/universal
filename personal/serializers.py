from rest_framework import serializers
from .models import Person, Address

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'full_name', 'prefix_title', 'gender']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'  # or list the fields you want to include
