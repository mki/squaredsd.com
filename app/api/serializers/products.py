from rest_framework import serializers

from products.models import Products


class ProductsRequestSerializer(serializers.Serializer):
    date_from = serializers.DateField(required=False)
    date_to = serializers.DateField(required=False)


class ProductsResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'created', 'owner')
