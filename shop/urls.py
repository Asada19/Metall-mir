from django.urls import path
from .views import CatalogListAPIView, CatalogDetailAPIView, ItemsListAPIView, ItemDetailAPIView, \
    CatalogDescriptionAPIView, OurClientsLogoAPIView, OurProvidersLogoAPIView, MainPriceFileAPIView

urlpatterns = [
    path('catalog/', CatalogListAPIView.as_view(), name='catalog list'),
    path('catalog/<int:pk>/', CatalogDescriptionAPIView.as_view(), name='catalog detail'),
    path('catalog_items/<int:pk>/', CatalogDetailAPIView.as_view(), name='catalog items'),
    path('items/', ItemsListAPIView.as_view(), name='items list'),
    path('items/<int:pk>', ItemDetailAPIView.as_view(), name='items detail'),
    path('providers_logo/', OurProvidersLogoAPIView.as_view(), name='providers logos'),
    path('clients_logo/', OurClientsLogoAPIView.as_view(), name='clients logos'),
    path('main_price_file', MainPriceFileAPIView.as_view(), name='main price file')
]

