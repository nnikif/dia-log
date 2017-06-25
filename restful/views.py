from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DialogueSerializer
from .models import Dialogue

# Create your views here.

class DialogueViewSet(viewsets.ModelViewSet):
    queryset = Dialogue.objects.all()
    serializer_class = DialogueSerializer
    http_method_names = ['get', 'post', 'head']