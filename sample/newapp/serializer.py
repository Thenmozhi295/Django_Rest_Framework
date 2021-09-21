from rest_framework import serializers
from newapp.models import health

class healthSerializer(serializers.ModelSerializer):
    class Meta:
        model = health
        fields = ['fruit','size','color']