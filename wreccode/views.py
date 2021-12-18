from django.db.models.query import QuerySet
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from .models import Responses
from .serializers import ResponseSerializer
from rest_framework.response import Response



class ResponseApiView(APIView):
    def get(self, request, pk):
        body = Responses.objects.all()
        serializer = ResponseSerializer(body, many=True)
        return Response(serializer.data)


    def post(self, request, pk):
        serializer = ResponseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        serializer = ResponseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)        

    def delete(self, request, pk):
        serializer = ResponseSerializer(data= request.data)
        if serializer.is_valid():
            a = Responses.objects.get(serializer.data)
            b = str(a)
            print(b)
            b.delete
            print(b)

            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
