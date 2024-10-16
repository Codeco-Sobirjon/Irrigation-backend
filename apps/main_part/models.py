from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields, TranslatableManager
from django_ckeditor_5.fields import CKEditor5Field


class AboutInstitution(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Название института"), max_length=250, null=True, blank=True),
    )
    year_of_admission = models.IntegerField(null=True, blank=True, default=2022, verbose_name="Год поступления")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")
    logo = models.ImageField(upload_to="media/logo", null=True, blank=True, verbose_name='Логотип института')

    objects = TranslatableManager()

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("1. Об институте")
        verbose_name_plural = _("1. Об институте")


class SliderMainPart(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Название слайдера"), max_length=250, null=True, blank=True),
    )
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")
    slider_image = models.ImageField(upload_to="media/slider", null=True, blank=True, verbose_name='Изб. слайдера')

    objects = TranslatableManager()

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("2. Главная страница слайдера")
        verbose_name_plural = _("2. Главная страница слайдера")


class Partners(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Название партнер"), max_length=250, null=True, blank=True),
        description=CKEditor5Field(config_name='extends', verbose_name="Краткое описание"),
    )
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")
    logo = models.ImageField(upload_to="media/logo", null=True, blank=True, verbose_name='Логотип партнер')

    objects = TranslatableManager()

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("3. Партнеры")
        verbose_name_plural = _("3. Партнеры")


class VideoInstitution(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Название видео"), max_length=250, null=True, blank=True),
    )
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")
    url_video = models.URLField(null=True, blank=True, verbose_name='URL-адрес видео для института')

    objects = TranslatableManager()

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("4. Видео")
        verbose_name_plural = _("4. Видео")


class Announcement(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Название объявления"), max_length=250, null=True, blank=True),
        description=CKEditor5Field(config_name='extends', verbose_name="Описание"),
    )
    logo = models.ImageField(upload_to='media/announcement', null=True, blank=True, verbose_name="Логотип")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = TranslatableManager()

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("5. Объявления")
        verbose_name_plural = _("5. Объявления")
