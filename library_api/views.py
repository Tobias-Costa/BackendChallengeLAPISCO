from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Authors, Books
from .serializers import authorsSerializer, booksSerializer

class Author(APIView):

    def get(self, request):
        obj = Authors.objects.all()
        serializer = authorsSerializer(obj, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        received_data=request.data
        serializer = authorsSerializer(data=received_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class AuthorByID(APIView):

    def get_object(self, id):
        return get_object_or_404(Authors, id=id)
        
    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = authorsSerializer(instance)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = authorsSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id=None):
        instance=self.get_object(id)
        serializer=authorsSerializer(instance)
        instance.delete()
        return Response(serializer.data)

