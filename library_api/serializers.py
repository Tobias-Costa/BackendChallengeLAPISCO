from rest_framework import serializers
from .models import Authors, Books

class authorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Authors
        fields = "__all__"

class booksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"