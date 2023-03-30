from .models import *
from rest_framework import serializers

class Accountserializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'


class Destinationserializer(serializers.ModelSerializer):
    class Meta:
        model=Destination
        fields='__all__'
        
