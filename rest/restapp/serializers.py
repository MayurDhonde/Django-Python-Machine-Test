# serializers.py
from rest_framework import serializers
from .models import *

class ClientSerializer(serializers.ModelSerializer):
    created_by= serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']

class ClientPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=[ 'client_name', 'created_by']

class ProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','project_name']

#get detail by id
class ClientDetailSerializer(serializers.ModelSerializer):
    projects = ProjectUserSerializer(many=True, read_only=True)
    created_by= serializers.CharField(source="created_by.username", read_only=True)
    update_at=serializers.DateTimeField(source='created_at')

    class Meta:
        model = Client
        fields = ('id', 'client_name', 'projects', 'created_at', 'created_by', 'update_at')  

class ProjectSerializer(serializers.ModelSerializer):
    client=serializers.CharField(source="client.client_name", read_only=True)
    created_by= serializers.CharField(source="created_by.username", read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'client','project_name', 'created_at', 'created_by' ]

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id','username']

class ProjectPostSerializer(serializers.ModelSerializer):
    client=serializers.CharField(source="client.client_name", read_only=True)
    created_by= serializers.CharField(source="created_by.username", read_only=True)
    class Meta:
        model = Project
        fields = ['id','client','project_name', 'users', 'created_by' ]
  

