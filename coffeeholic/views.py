from rest_framework import generics, permissions
from .models import CoffeeShop
from .serializers import CoffeeShopSerializer
from coffeeholic.permissions import IsOwnerReadOnly


class CoffeeShopList(generics.ListCreateAPIView):
    queryset = CoffeeShop.objects.all()
    serializers_class = CoffeeShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CoffeeShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoffeeShop.objects.all()
    serializers_class = CoffeeShopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
