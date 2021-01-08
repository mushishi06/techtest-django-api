from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from products.models import Product
from products.serializers import (ProductSerializer,
                                  ProductSerializerUpdate,
                                  ProductSerializerQty)

# Create your views here.


@permission_classes((permissions.AllowAny,))
@api_view(['GET', 'POST'])
def product_list(request, format=None):
    """List all Products, or create a new Product."""
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
@api_view(['GET'])
def product_list_available(request, format=None):
    """List all Products, or create a new Product."""
    if request.method == 'GET':
        product = Product.objects.filter(qty__gt=0)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
@api_view(['GET'])
def product_list_sold(request, format=None):
    """List all Products, or create a new Product."""
    if request.method == 'GET':
        product = Product.objects.filter(qty__lte=0)
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, slug, format=None):
    """Retrieve, update or delete a product."""
    try:
        product = Product.objects.get(sku=slug)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializerUpdate(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes((permissions.AllowAny,))
@api_view(['POST'])
def product_qty_change(request, format=None):
    """Retrieve, update or delete a product."""

    if request.method == 'POST':
        serializer = ProductSerializerQty(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            try:
                product = Product.objects.get(sku=serializer.data["sku"])
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            qty = serializer.data["qty"]
            print("qty= ", qty)
            product.qty = product.qty + qty
            product.save()
            return Response(ProductSerializer(product).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 3)List all available products (&gt;0 Qty)
# 4) List all sold out products (0 Qty)
# 5) Register Qty Change (SKU, +/- Value)
