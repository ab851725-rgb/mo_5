from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import(
    CategoryDetailSerializer,
    CategorySerializer,
    ProductDetailSerializer,
    ProductSerializer,
    ReviewDetailSerializer,
    ReviewSerializer,
    ProductReviewSerializer,
)     

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': 'category not found:('},
                        status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(category).data
    return Response(data=data)

@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    list_ = CategorySerializer(categories, many=True).data
    return Response(data=list_)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'product not found:('},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product).data
    return Response(data=data)

@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    list_ = ProductSerializer(products, many=True).data
    return Response(data=list_)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found:('},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(Review).data
    return Response(data=data)

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    list_ = ReviewSerializer(reviews, many=True).data
    return Response(data=list_)

@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    data = ProductReviewSerializer(products, many=True).data
    return Response(data=data)