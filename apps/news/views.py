from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.news.filters import NewsFilterSet
from apps.news.models import (
    News,
    NewsImages,
    Comment, AchievementsCategory,
    AchievementsQuality
)
from apps.news.pagination import NewsPagination
from apps.news.serializers import (
    NewsSerializer, AchievementsQualityListSerialzier, AchievementsCategoryListSerializer
)


class NewsListView(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterSet
    pagination_class = NewsPagination

    @swagger_auto_schema(
        tags=['News'],
        manual_parameters=[
            openapi.Parameter('category', openapi.IN_QUERY, description="Фильтр по идентификатору категории",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('title', openapi.IN_QUERY, description="Фильтр по названию (без учета регистра)",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('page_size', openapi.IN_QUERY, description="Количество элементов на странице",
                              type=openapi.TYPE_INTEGER),
            openapi.Parameter('is_three_menu_news', openapi.IN_QUERY, description="Три новости для меню, 3 новые новости с конца",
                              type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('is_four_menu_news', openapi.IN_QUERY, description="Четыре новости для меню, еще 4 новости через 3 с конца",
                              type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('is_announcements', openapi.IN_QUERY,
                              description="Фильтрует новости для отображения актуальных объявлений и обновлений.",
                              type=openapi.TYPE_BOOLEAN),
        ],
        responses={200: NewsSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        queryset = News.objects.all()
        filterset = self.filterset_class(request.GET, queryset=queryset)
        if not filterset.is_valid():
            return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

        paginator = self.pagination_class()  # Create an instance of the pagination class
        paginated_queryset = paginator.paginate_queryset(filterset.qs, request)
        serializer = NewsSerializer(paginated_queryset, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)


class AchievementsCategoryListView(APIView):

    @swagger_auto_schema(tags=['Achievements Quality'], responses={200: AchievementsCategoryListSerializer(many=True)})
    def get(self, request):
        instance = AchievementsCategory.objects.all()
        serializer = AchievementsCategoryListSerializer(instance, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsDetailsView(APIView):

    @swagger_auto_schema(tags=['News'], responses={200: NewsSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        queryset = get_object_or_404(News, id=kwargs.get('id'))
        serializer = NewsSerializer(queryset, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

