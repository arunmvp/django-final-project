from rest_framework import serializers
from .models import *

class userinfoserializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields = "__all__" 
        
        
