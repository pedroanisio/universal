# Dentro de mailbox/urls.py

from django.urls import path
from mailbox.api.views import EmailAPIView

urlpatterns = [
    path('emails', EmailAPIView.as_view(), name='email-create-endpoint'), 
]
