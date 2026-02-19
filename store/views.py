from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin

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
