from django.shortcuts import get_object_or_404
from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from apps.news.models import (
    News,
    NewsImages,
    Comment,
    Staffs, Postions,
    ContactInfo,
    InfoAboutInstitution,
    AchievementsCategory,
    AchievementsQuality
)
from apps.menu.serializers import (
    TertiaryCategorySerializer,
    SubCategorySerializer,
    TopLevelCategory
)
from apps.menu.models import Category


class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImages
        fields = ['id', 'news', 'image']


class CommentNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'description', 'created_at']


class NewsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)
    images_list = serializers.SerializerMethodField()
    categories_list = serializers.SerializerMethodField()
    comments_list = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'translations', 'categories_list', 'viewers', 'video_url', 'images_list', 'created_at',
                  'comments_list']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }

    def get_images_list(self, obj):
        queryset = NewsImages.news_image.filter_by_news(obj)
        serializer = NewsImageSerializer(queryset, many=True, context={'request': self.context.get('request')})
        return serializer.data

    def get_categories_list(self, obj):
        categories = obj.category.all()
        list_category = []

        def find_main_category(category):
            if category.parent is None:
                return category
            return find_main_category(category.parent)

        def build_category_hierarchy(category):
            path = []
            current_category = category

            while current_category:
                path.insert(0, {
                    "id": current_category.id,
                    "name": current_category.safe_translation_getter('name', any_language=True)
                })
                current_category = current_category.parent

            return path

        for category in categories:

            main_category = find_main_category(category)

            hierarchy = build_category_hierarchy(category)

            list_category.append({
                "main_category": {
                    "id": main_category.id,
                    "name": main_category.safe_translation_getter('name', any_language=True)
                },
                "full_hierarchy": hierarchy
            })

        return list_category

    def get_comments_list(self, obj):
        queryset = Comment.news_comment.filter_by_news(obj)
        serializer = CommentNewsSerializer(queryset, many=True, context={'request': self.context.get('request')})
        return serializer.data


class PositionListSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Postions)

    class Meta:
        model = Postions
        fields = ['id', 'translations']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class StaffListSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Staffs)
    position = PositionListSerializer(read_only=True)

    class Meta:
        model = Staffs
        fields = ['id', 'translations', 'position', 'image', 'created_at']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class ContactInfoListSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=ContactInfo)

    class Meta:
        model = ContactInfo
        fields = ['id', 'translations', 'created_at']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class InfoAboutInstitutionListSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=InfoAboutInstitution)

    class Meta:
        model = InfoAboutInstitution
        fields = ['id', 'translations', 'created_at']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class AchievementsCategoryListSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=AchievementsCategory)
    qualities = serializers.SerializerMethodField()

    class Meta:
        model = AchievementsCategory
        fields = ['id', 'translations', 'qualities', 'created_at']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }

    def get_qualities(self, obj):
        queryset = AchievementsQuality.objects.select_related('achievements_category').filter(
            achievements_category=obj
        )
        serializer = AchievementsQualityListSerialzier(queryset, many=True, context={'request': self.context.get('request')})
        return serializer.data


class AchievementsQualityListSerialzier(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=AchievementsQuality)

    class Meta:
        model = AchievementsQuality
        fields = ['id', 'translations', 'level', 'created_at']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }