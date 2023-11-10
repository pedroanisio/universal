from rest_framework import viewsets
from personal.models import Person, Address
from personal.serializers import PersonSerializer, AddressSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned addresses to a given person,
        by filtering against a `person_id` query parameter in the URL.
        """
        queryset = Address.objects.all()
        person_id = self.request.query_params.get('person_id', None)
        if person_id is not None:
            queryset = queryset.filter(person_id=person_id)
        return queryset
