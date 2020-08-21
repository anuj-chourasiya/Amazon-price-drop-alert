from django.shortcuts import render
from rest_framework.viewsets  import ModelViewSet
from .models import Info
from restapp.serializers import RestSerializer

class RestViewSet(ModelViewSet):
    queryset=Info.objects.all()
    serializer_class=RestSerializer


