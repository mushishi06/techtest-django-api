from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.Serializer):
    """Product object."""

    # id = serializers.IntegerField(read_only=True)
    sku = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    name = serializers.CharField(required=True, allow_blank=False, max_length=255)
    qty = serializers.IntegerField(required=True)
    price = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)

    def create(self, validated_data):
        """Create and return a new `Product` instance, given the validated data."""
        return Product.objects.create(**validated_data)


class ProductSerializerUpdate(serializers.Serializer):
    """Product object."""

    # id = serializers.IntegerField(read_only=True)
    sku = serializers.CharField(required=False, allow_blank=False, max_length=1000)
    name = serializers.CharField(required=False, allow_blank=False, max_length=255)
    qty = serializers.IntegerField(required=True)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)

    def update(self, instance, validated_data):
        """Update and return an existing `Product` instance, given the validated data."""
        instance.sku = validated_data.get('sku', instance.sku)
        instance.name = validated_data.get('name', instance.name)
        instance.qty = validated_data.get('qty', instance.qty)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductSerializerQty(serializers.Serializer):
    """Product object."""

    # id = serializers.IntegerField(read_only=True)
    sku = serializers.CharField(required=True, allow_blank=False, max_length=1000)
    name = serializers.CharField(required=False, allow_blank=False, max_length=255)
    qty = serializers.IntegerField(required=True)
    price = serializers.DecimalField(required=False, max_digits=10, decimal_places=2)
