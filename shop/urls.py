from django.urls import path
from .views import (CatalogListAPIView, CatalogDetailAPIView, ItemsListAPIView, ItemDetailAPIView,
                    CatalogDescriptionAPIView)

urlpatterns = [
    path('catalog/', CatalogListAPIView.as_view(), name='catalog list'),
    path('catalog/<int:pk>/', CatalogDescriptionAPIView.as_view(), name='catalog detail'),
    path('catalog_items/<int:pk>/', CatalogDetailAPIView.as_view(), name='catalog items'),
    path('items/', ItemsListAPIView.as_view(), name='items list'),
    path('items/<int:pk>', ItemDetailAPIView.as_view(), name='items detail')
]

