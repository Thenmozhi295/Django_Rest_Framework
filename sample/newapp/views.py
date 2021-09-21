from django.shortcuts import render
from rest_framework import generics
from newapp.models import health
from .serializer import healthSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class healthRegister(APIView):
    def get(self, request, format=None):
        snippets = health.objects.all()
        serializer = healthSerializer(snippets, many=True)
        return Response({'value':serializer.data})
