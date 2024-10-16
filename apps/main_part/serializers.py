from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from apps.main_part.models import (
    AboutInstitution,
    SliderMainPart,
    Partners,
    VideoInstitution,
    Announcement
)


class AboutInstitutionSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=AboutInstitution)

    class Meta:
        model = AboutInstitution
        fields = ['id', 'year_of_admission', 'created_at', 'logo', "translations"]

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class SliderMainPartSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=SliderMainPart)

    class Meta:
        model = SliderMainPart
        fields = ['id', 'created_at', 'slider_image', "translations"]

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class PartnersSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Partners)

    class Meta:
        model = Partners
        fields = ['id', 'created_at', 'logo', "translations"]

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class VideoInstitutionSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=VideoInstitution)

    class Meta:
        model = VideoInstitution
        fields = ['id', 'created_at', 'url_video', "translations"]

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }


class AnnouncementSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Announcement)

    class Meta:
        model = Announcement
        fields = ['id', 'created_at', 'logo', "translations"]

    def get_text(self, instance):
        return {
            "uz": instance.name_ru,
            "en": instance.name_en,
            "ru": instance.name_uz,
        }