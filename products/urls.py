from django.db import router
from django.urls import path
from django.urls.conf import include
from .views import ProductView, BrandView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', ProductView, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('brands/', BrandView.as_view(), name='brand_view'),
]
