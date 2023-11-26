from django.shortcuts import render
from rest_framework import generics
from .models import Client
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

#GET client
class ClientListAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#POST Client
class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientPostSerializer

# Get  Client by Id
class ClientDetailAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientDetailSerializer  # Serializer including nested projects

#Put Client
class ClientUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

#DELETE client
class ClientDeleteAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


#project view
class ProjectCreateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectPostSerializer

class UserProjectsListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(created_by=user)
        

        