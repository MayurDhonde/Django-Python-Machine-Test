from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display=['id','client_name', 'created_by', 'created_at']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','client', 'project_name', 'created_at', 'created_by']
