from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 20
    page_query_param = "p"          # renombrado
    page_size_query_param = "size"  # renombrado
    max_page_size = 100