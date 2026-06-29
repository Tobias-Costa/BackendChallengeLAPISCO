from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Authors, Books
from .serializers import authorsSerializer, booksSerializer
from .paginator import CustomPagination

class Author(APIView):
    """Gerencia a listagem e criação global de autores."""

    def get(self, request):
        """Lista todos os autores com paginação."""
        obj = Authors.objects.all()
        paginator = CustomPagination()
        page = paginator.paginate_queryset(obj, request)
        if page is not None:
            serializer = authorsSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        # Em caso de erro do paginator, retorna serializer padrão
        serializer = authorsSerializer(obj, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        """Valida e cria um novo autor."""
        received_data=request.data
        serializer = authorsSerializer(data=received_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class AuthorByID(APIView):
    """Gerencia operações individuais (GET, PUT, DELETE) de um autor por ID."""
    
    def get_object(self, id):
        """Busca o autor ou retorna erro 404 caso não exista."""
        return get_object_or_404(Authors, id=id)
        
    def get(self, request, id=None):
        """Retorna os dados de um autor específico."""
        instance = self.get_object(id)
        serializer = authorsSerializer(instance)
        return Response(serializer.data)
    
    def put(self, request, id=None):
        """Atualiza os dados de um autor específico."""
        data = request.data
        instance = self.get_object(id)
        serializer = authorsSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id=None):
        """Exclui um autor e retorna os dados do registro deletado."""
        instance=self.get_object(id)
        serializer=authorsSerializer(instance)
        instance.delete()
        return Response(serializer.data)

class Book(APIView):
    """Gerencia a listagem, filtragem e criação global de livros."""

    def get_authors(self, serializer_data, is_many):
        """Injeta dinamicamente ID e nome dos autores no JSON gerado pelo serializer."""
        if is_many:
            for book_data in serializer_data:
                book_obj = Books.objects.prefetch_related("authors").get(id=book_data["id"])
                book_data["authors"] = [{"id":author.id, "name":author.name} for author in book_obj.authors.all() ]
        else:
            book_obj = Books.objects.prefetch_related("authors").get(id=serializer_data["id"])
            serializer_data["authors"] =  [{"id":author.id, "name":author.name} for author in book_obj.authors.all() ]
          
        return serializer_data

    def get(self, request):
        """Filtra, ordena por título, pagina e lista os livros."""
        # Setup dos objetos e do paginator
        obj = Books.objects.all().prefetch_related("authors")
        paginator = CustomPagination()
        # Parâmetros de filtragem
        title = self.request.query_params.get("title")
        author = self.request.query_params.get("author")
        # Filtragem
        if author is not None:
            obj = obj.filter(authors__name__icontains=author)

        if title is not None:
            obj = obj.filter(title__icontains=title)

        # Evita livros duplicados após filtragem
        obj = obj.distinct().order_by("title")

        # Paginação
        page = paginator.paginate_queryset(obj, request)
        if page is not None:
            serializer = booksSerializer(page, many=True)
            serializer_data = self.get_authors(serializer.data, is_many=True)
            return paginator.get_paginated_response(serializer_data)
        # Caso dê erro na paginação, retorna serializer padrão
        serializer = booksSerializer(obj, many=True)
        serializer_data = self.get_authors(serializer.data, is_many=True)
        return Response(serializer_data, status=200)

    def post(self, request):
        """Cria um livro e injeta seus autores na resposta de sucesso."""
        received_data=request.data
        serializer = booksSerializer(data=received_data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = self.get_authors(serializer.data, is_many=False)
            return Response(serializer_data, status=201)
        return Response(serializer.errors, status=400)
    
class BookByID(APIView):
    """Gerencia operações individuais (GET, PUT, DELETE) de um livro por ID."""

    def get_authors(self, serializer_data):
        """Injeta os autores no JSON de um único livro."""
        book_obj = Books.objects.prefetch_related("authors").get(id=serializer_data["id"])
        serializer_data["authors"] = [{"id":author.id, "name":author.name} for author in book_obj.authors.all()]
        return serializer_data

    def get_object(self, id):
        """Busca o livro ou retorna erro 404."""
        return get_object_or_404(Books, id=id)
        
    def get(self, request, id=None):
        """Retorna os dados de um livro específico com seus autores."""
        instance = self.get_object(id)      
        serializer = booksSerializer(instance)
        serializer_data = self.get_authors(serializer.data)
        return Response(serializer_data, status=200)
    
    def put(self, request, id=None):
        """Atualiza um livro e retorna seus dados atualizados com os autores."""
        data = request.data
        instance = self.get_object(id)
        serializer = booksSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            serializer_data = self.get_authors(serializer.data)
            return Response(serializer_data, status=200)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id=None):
        """Exclui um livro e retorna o JSON do registro deletado."""
        instance=self.get_object(id)
        serializer=booksSerializer(instance)
        instance.delete()
        return Response(serializer.data)
