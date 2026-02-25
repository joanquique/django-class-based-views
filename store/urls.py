from django.urls import path

from .views import (
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProtectedListView, ProductListAPI, MyProfileView
)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("my-products/", ProtectedListView.as_view(), name="my_products"),
    path("api/products/", ProductListAPI.as_view(), name="api_products"),
    path("api/token/", obtain_auth_token, name="api_token"),
    path("api/me/", MyProfileView.as_view(), name="api_me"),
]
