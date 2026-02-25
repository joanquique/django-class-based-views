from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.pagination import PageNumberPagination

from rest_framework.generics import ListAPIView

from .models import Product
from .serializers import ProductSerializer
from .pagination import ProductPagination

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ProductPagination(PageNumberPagination):
    page_size = 20
    page_query_param = "p"          # renombrado
    page_size_query_param = "size"  # renombrado
    max_page_size = 100

class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"

class ProductCreateView(CreateView):
    model = Product
    template_name = "store/product_form.html"
    fields = ["title", "price", "description", "seller", "color", "product_dimensions"]
    success_url = reverse_lazy("product_list")

class ProductUpdateView(UpdateView):
    model = Product
    template_name = "store/product_form.html"
    fields = ["title", "price", "description", "seller", "color", "product_dimensions"]
    success_url = reverse_lazy("product_list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "store/product_confirm_delete.html"
    success_url = reverse_lazy("product_list")

class ProtectedListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "store/my_products.html"
    context_object_name = "products"
    login_url = "/login/"

    def get_queryset(self):
        return Product.objects.filter(owner=self.request.user).order_by("-id")

class ProductListAPI(ListAPIView):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    
class MyProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })