from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet  # Importe suas viewsets aqui

# Criar um roteador e registrar suas viewsets
router = DefaultRouter()
router.register(r'people', PersonViewSet)

# As URLs da API são determinadas automaticamente pelo roteador
urlpatterns = [
    path('', include(router.urls)),
]
