from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import CatalogSerializer, ItemSerializer, CatalogDetailSerializer, CatalogDescriptionSerializer, \
    OurClientsLogoSerializer, OurProvidersLogoSerializer
from .models import Catalog, Item, ItemField, OurClientsLogo, OurProvidersLogo


class CatalogListAPIView(ListAPIView):
    serializer_class = CatalogSerializer
    model = Catalog
    queryset = Catalog.objects.all()


class CatalogDetailAPIView(RetrieveAPIView):
    serializer_class = CatalogDetailSerializer
    model = Catalog
    queryset = Catalog.objects.all()


class CatalogDescriptionAPIView(RetrieveAPIView):
    serializer_class = CatalogDescriptionSerializer
    model = Catalog
    queryset = Catalog.objects.all()


class ItemsListAPIView(ListAPIView):
    serializer_class = ItemSerializer
    model = Item
    queryset = Item.objects.all()


class ItemDetailAPIView(RetrieveAPIView):
    serializer_class = ItemSerializer
    model = Item
    queryset = Item.objects.all()


class OurClientsLogoAPIView(ListAPIView):
    serializer_class = OurClientsLogoSerializer
    model = OurClientsLogo
    queryset = OurClientsLogo.objects.all()


class OurProvidersLogoAPIView(ListAPIView):
    serializer_class = OurProvidersLogoSerializer
    model = OurProvidersLogo
    queryset = OurProvidersLogo.objects.all()
