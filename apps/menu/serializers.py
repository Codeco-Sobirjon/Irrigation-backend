from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from apps.menu.models import (
    Category,
    TopLevelCategory,
    SubCategory,
    TertiaryCategory
)


class TertiaryCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=TertiaryCategory)

    class Meta:
        model = TertiaryCategory
        fields = ['id', 'is_news', 'is_staff', 'is_contact', 'translations']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class SubCategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SubCategory)
    tertiary_categories = serializers.SerializerMethodField()

    class Meta:
        model = SubCategory
        fields = ['id', 'is_news', 'is_staff', 'is_contact', 'translations', 'tertiary_categories']

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }

    def get_tertiary_categories(self, obj):
        tertiary_categories = TertiaryCategory.objects.filter(parent=obj)
        return TertiaryCategorySerializer(tertiary_categories, many=True, context=self.context).data


class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'is_news', 'is_staff', 'is_contact', 'created_at', 'translations', 'subcategories']

    def get_text(self, instance):
        return {
            "uz": instance.safe_translation_getter('name', language_code='uz'),
            "en": instance.safe_translation_getter('name', language_code='en'),
            "ru": instance.safe_translation_getter('name', language_code='ru'),
        }
