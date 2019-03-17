from django.shortcuts import render
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """Manage note"""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Create your views here.
