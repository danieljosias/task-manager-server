from rest_framework import generics
from .models import List
from .serializers import ListSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import AuthenticatedOrReadOnly


class ListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AuthenticatedOrReadOnly]

    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListViewDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AuthenticatedOrReadOnly]

    lookup_url_kwarg = 'list_id'

    queryset = List.objects.all()
    serializer_class = ListSerializer