from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import *

# Create your views here.


class crudInfo(APIView):
    def post(self, request):
        serializers = userinfoserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id):
        try:
            if user_id:
                user = userinfo.objects.get(user_id=user_id)
                serializer = userinfoserializer(user)
                return Response(serializer.data, status=status.HTTP_302_FOUND)
            else:
                user = userinfo.objects.all()
                serializer = userinfoserializer(user, many=True)
                return Response(serializer.data, status=status.HTTP_302_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
