from rest_framework import serializers
from .models import CoffeeShop


class CoffeeShopSerializer(serializers.HyperlinkedModelSerializer):
    coffeeshop_url = serializers.ModelSerializer.serializer_url_field(
        view_name='coffeeshop_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CoffeeShop
        fields = ('id', 'name', 'city', 'state', 'coffeeshop_url',
                  'website_url', 'photo_url', 'memo', 'posted', 'owner')
