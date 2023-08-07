from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer


class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
