from django.db import models

class Authors(models.Model):
    '''Tabela de autores de livros'''
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    bio = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "authors"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Books(models.Model):
    '''Tabela de livros'''
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Authors)

    class Meta:
        db_table = "books"
        ordering = ["title", "-publication_date"]

    def __str__(self):
        return self.title
    