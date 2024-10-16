from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields, TranslatableManager
from django_ckeditor_5.fields import CKEditor5Field


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Название категория"), max_length=250, null=True, blank=True),
    )
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="Родитель категории", related_name='subcategories')
    is_news = models.BooleanField(default=False, null=True, blank=True, verbose_name="Это новости")
    is_staff = models.BooleanField(default=False, null=True, blank=True, verbose_name="Это персонал")
    is_contact = models.BooleanField(default=False, null=True, blank=True, verbose_name="Это контакт")

    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = TranslatableManager()

    def __str__(self):
        str_name = self.safe_translation_getter('name', any_language=True)
        parent = self.parent

        while parent:
            str_name = f'{parent.safe_translation_getter("name", any_language=True)} / ' + str_name
            parent = parent.parent

        return str_name

    class Meta:
        ordering = ["id"]
        verbose_name = _("Об институте")
        verbose_name_plural = _("Об институте")


class TopLevelCategory(Category):
    class Meta:
        proxy = True
        verbose_name = "1. Основная категория"
        verbose_name_plural = "1. Основная категория"


class SubCategory(Category):
    class Meta:
        proxy = True
        verbose_name = "2. Подкатегория"
        verbose_name_plural = "2. Подкатегория"


class TertiaryCategory(Category):
    class Meta:
        proxy = True
        verbose_name = "3. Третичная категория"
        verbose_name_plural = "3. Третичная категория"

