from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from apps.main_part.models import (
    AboutInstitution,
    SliderMainPart,
    Partners,
    VideoInstitution, Announcement
)
from apps.main_part.pagination import AnnouncementPagination
from apps.main_part.serializers import (
    AboutInstitutionSerializer,
    SliderMainPartSerializer,
    PartnersSerializer,
    VideoInstitutionSerializer,
    AnnouncementSerializer
)


class AboutInstitutionListView(APIView):

    @swagger_auto_schema(tags=['Main Part'], responses={200: AboutInstitutionSerializer(many=True)})
    def get(self, request):
        instance = AboutInstitution.objects.all()
        serializer = AboutInstitutionSerializer(instance, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class SliderMainPartListView(APIView):

    @swagger_auto_schema(tags=['Main Part'], responses={200: SliderMainPartSerializer(many=True)})
    def get(self, request):
        instance = SliderMainPart.objects.all().order_by('-id')
        serializer = SliderMainPartSerializer(instance, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PartnersListView(APIView):

    @swagger_auto_schema(tags=['Main Part'], responses={200: PartnersSerializer(many=True)})
    def get(self, request):
        instance = Partners.objects.all().order_by('-id')
        serializer = PartnersSerializer(instance, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class VideoInstitutionListView(APIView):

    @swagger_auto_schema(tags=['Main Part'], responses={200: VideoInstitutionSerializer(many=True)})
    def get(self, request):
        instance = VideoInstitution.objects.all().order_by('-id')
        serializer = VideoInstitutionSerializer(instance, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnnouncementListView(APIView):
    pagination_class = AnnouncementPagination

    @swagger_auto_schema(tags=['Main Part'], responses={200: AnnouncementSerializer(many=True)})
    def get(self, request):
        instance = Announcement.objects.all().order_by('-id')
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(instance, request)
        serializer = AnnouncementSerializer(paginated_queryset, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
