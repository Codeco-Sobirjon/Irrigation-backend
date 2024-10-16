from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.menu.models import (
    Category,
    TopLevelCategory,
    SubCategory,
    TertiaryCategory
)
from apps.menu.serializers import (
    CategorySerializer
)
from apps.news.filters import NewsFilterSet
from apps.news.models import (
    News, Staffs, ContactInfo,
    InfoAboutInstitution
)
from apps.news.pagination import NewsPagination
from apps.news.serializers import (
    NewsSerializer,
    StaffListSerializer, ContactInfoListSerializer,
    InfoAboutInstitutionListSerializer
)


class CategoryListView(APIView):

    @swagger_auto_schema(tags=['Categories'], responses={200: CategorySerializer(many=True)})
    def get(self, request):
        instance = Category.objects.select_related('parent').filter(parent__isnull=True)
        serializer = CategorySerializer(instance, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetailView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterSet
    pagination_class = NewsPagination

    @swagger_auto_schema(
        tags=['Categories'],
        manual_parameters=[
            openapi.Parameter('is_news', openapi.IN_QUERY, description="Фильтр по категории новостей",
                              type=openapi.TYPE_BOOLEAN, default=False),
            openapi.Parameter('is_staff', openapi.IN_QUERY, description="Фильтр по персоналу",
                              type=openapi.TYPE_BOOLEAN, default=False),
            openapi.Parameter('is_contact', openapi.IN_QUERY, description="Фильтр по категории контактов",
                              type=openapi.TYPE_BOOLEAN, default=False),
        ],
        responses={200: CategorySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        cat_id = kwargs.get('id')
        is_news = request.query_params.get('is_news', 'false').lower() == 'true'
        is_staff = request.query_params.get('is_staff', 'false').lower() == 'true'
        is_contact = request.query_params.get('is_contact', 'false').lower() == 'true'
        queryset = get_object_or_404(Category, id=cat_id)

        if is_news and queryset.is_news:
            return self.is_news_cat(queryset, request)

        if is_staff and queryset.is_staff:
            return self.is_staff_cat(queryset, request)

        if is_contact and queryset.is_contact:
            return self.is_contact_cat(queryset, request)

        querysets = InfoAboutInstitution.objects.prefetch_related('category').filter(category=queryset.id)
        serializer = InfoAboutInstitutionListSerializer(querysets, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def is_news_cat(self, queryset, request):
        if queryset.is_news:
            news_queryset = News.categories.filter_by_category(queryset.id)
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(news_queryset, request)
            serializer = NewsSerializer(paginated_queryset, many=True, context={'request': request})
            return paginator.get_paginated_response(serializer.data)
        return Response([], status=status.HTTP_404_NOT_FOUND)  # If not a news category, return 404

    def is_staff_cat(self, queryset, request):
        if queryset.is_staff:
            staff_queryset = Staffs.categories.filter_by_category(queryset.id)
            serializer = StaffListSerializer(staff_queryset, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_404_NOT_FOUND)  # If not a staff category, return 404

    def is_contact_cat(self, queryset, request):
        if queryset.is_contact:
            contact_info_queryset = ContactInfo.categories.filter_by_category(queryset.id)
            serializer = ContactInfoListSerializer(contact_info_queryset, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_404_NOT_FOUND)

