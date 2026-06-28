from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Authors, Books
from .serializers import authorsSerializer, booksSerializer
from .paginator import CustomPagination

class Author(APIView):

    def get(self, request):
        obj = Authors.objects.all()
        paginator = CustomPagination()
        page = paginator.paginate_queryset(obj, request)
        if page is not None:
            serializer = authorsSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
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

class Book(APIView):

    def get_authors(self, serializer_data, obj):
        '''obtêm dados de autores através do id'''
        try:
            for book_data, obj_data in zip(serializer_data, obj):
                book_data["authors"] = [{"id":author.id, "name":author.name} for author in obj_data.authors.all() ]
        except TypeError:
            serializer_data["authors"] =  [{"id":author.id, "name":author.name} for author in obj.authors.all() ]
          
        return serializer_data

    def get(self, request):
        obj = Books.objects.all().prefetch_related("authors")
        paginator = CustomPagination()
        page = paginator.paginate_queryset(obj, request)
        if page is not None:
            serializer = booksSerializer(page, many=True)
            serializer_data = self.get_authors(serializer.data, obj)
            return paginator.get_paginated_response(serializer_data)

        serializer = booksSerializer(obj, many=True)
        serializer_data = self.get_authors(serializer.data, obj)
        return Response(serializer_data, status=200)

    def post(self, request):
        received_data=request.data
        serializer = booksSerializer(data=received_data)
        if serializer.is_valid():
            obj = serializer.save()
            serializer_data = self.get_authors(serializer.data, obj)
            return Response(serializer_data, status=201)
        return Response(serializer.errors, status=400)
    
class BookByID(APIView):

    def get_authors(self, serializer_data, obj):
        '''Obtêm dados de autores através do id'''
        serializer_data["authors"] = [{"id":author.id, "name":author.name} for author in obj.authors.all()]
        return serializer_data

    def get_object(self, id):
        return get_object_or_404(Books, id=id)
        
    def get(self, request, id=None):
        instance = self.get_object(id)      
        serializer = booksSerializer(instance)
        serializer_data = self.get_authors(serializer.data, instance)
        return Response(serializer_data, status=200)
    
    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = booksSerializer(instance, data=data)
        if serializer.is_valid():
            obj = serializer.save()
            serializer_data = self.get_authors(serializer.data, obj)
            return Response(serializer_data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id=None):
        instance=self.get_object(id)
        serializer=booksSerializer(instance)
        instance.delete()
        return Response(serializer.data)
