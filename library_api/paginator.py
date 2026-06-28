from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    '''Classe de paginação customizada'''
    page_size=5
    page_query_param="page"
    max_page_size=100