from rest_framework.views import APIView
from rest_framework.response import Response
from mailbox.api.serializers import EmailPostSerializer

class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = EmailPostSerializer(data=request.data)
        if serializer.is_valid():
            email_header = serializer.save()
            return Response({"message": "Email created successfully", "email_id": email_header.id}, status=201)
        return Response(serializer.errors, status=400)
