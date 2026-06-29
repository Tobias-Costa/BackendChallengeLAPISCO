from rest_framework import serializers
from .models import Authors, Books

class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = "__all__"

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"