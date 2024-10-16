from django.db import models
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields, TranslatableManager
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import URLValidator
from apps.menu.models import (
    Category
)
from apps.news.validation import validate_http_https
from apps.news.manager.news_manager import NewsManager, NewsImagesManager, CommentManager, StaffManager, \
    CommentInfoManager


class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Название заголовок"), max_length=250, null=True, blank=True),
        description=CKEditor5Field(config_name='extends', verbose_name="Краткое описание"),
    )
    category = models.ManyToManyField(Category, null=True, blank=True,
                                      verbose_name='Категория', related_name="category_news")
    viewers = models.IntegerField(default=0, null=True, blank=True, verbose_name="Зрители")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")
    video_url = models.URLField(null=True, blank=True, verbose_name='URL-адрес видео',
                                validators=[URLValidator(), validate_http_https])
    objects = TranslatableManager()
    categories = NewsManager()

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("4. Новости")
        verbose_name_plural = _("4. Новости")


class NewsImages(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='тип новости', related_name='news_image')
    image = models.ImageField(upload_to='media/news_image', null=True, blank=True, verbose_name='Новостные картинки')

    objects = models.Manager()
    news_image = NewsImagesManager()

    class Meta:
        ordering = ["id"]
        verbose_name = _("Новостные картинки")
        verbose_name_plural = _("Новостные картинки")


class Comment(models.Model):
    full_name = models.CharField(_('Полное имя'), max_length=250, null=True, blank=True)
    description = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True,
                             verbose_name='тип новости', related_name='news_comment')
    is_moderator = models.BooleanField(default=False, null=True, blank=True, verbose_name="Пропуск модератора")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = TranslatableManager()
    news_comment = CommentManager()

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ["id"]
        verbose_name = _("5. Комментарий")
        verbose_name_plural = _("5. Комментарий")


class Postions(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_(""), max_length=250, null=True, blank=True),
    )

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("1. Должность")
        verbose_name_plural = _("1. Должность")


class Staffs(TranslatableModel):
    translations = TranslatedFields(
        full_name=models.CharField(_("Полное имя"), max_length=250, null=True, blank=True),
        work_date=models.CharField(_("Рабочая дата"), max_length=250, null=True, blank=True),
        private_phone=models.CharField(_("Личный телефон"), max_length=250, null=True, blank=True),
        comapany_phone=models.CharField(_("Рабочий телефон"), max_length=250, null=True, blank=True),
        adress=models.CharField(_("Адрес"), max_length=250, null=True, blank=True),
        email=models.CharField(_("Электронная почта"), max_length=250, null=True, blank=True, unique=True),
        work_activity=CKEditor5Field(config_name='extends', verbose_name="Рабочая деятельность"),
        scientific_activity=CKEditor5Field(config_name='extends', verbose_name="Научная деятельность"),
    )
    position = models.ForeignKey(Postions, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Должность",
                                 related_name="position_staff")
    category = models.ManyToManyField(Category, null=True, blank=True,
                                      verbose_name='Категория', related_name="category_staff")
    is_leadership = models.BooleanField(default=False, null=True, blank=True, verbose_name="Это лидерство")
    image = models.ImageField(upload_to='media/staff', null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = TranslatableManager()
    categories = StaffManager()

    def __str__(self):
        return self.safe_translation_getter('full_name', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("2. Сотрудники университета")
        verbose_name_plural = _("2. Сотрудники университета")


class ContactInfo(TranslatableModel):
    translations = TranslatedFields(
        adress=models.CharField(_("Адрес"), max_length=250, null=True, blank=True),
        comapany_phone=models.CharField(_("Рабочий телефон"), max_length=250, null=True, blank=True),
        faks=models.CharField(_("Факсы"), max_length=250, null=True, blank=True),
        email=models.CharField(_("Электронная почта"), max_length=250, null=True, blank=True, unique=True),
    )
    category = models.ManyToManyField(Category, null=True, blank=True,
                                      verbose_name='Категория', related_name="category_contact_info")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = TranslatableManager()
    categories = CommentInfoManager()

    def __str__(self):
        return self.safe_translation_getter('adress', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("3. Контактная информация института")
        verbose_name_plural = _("3. Контактная информация института")


class InfoAboutInstitution(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Заголовок"), max_length=250, null=True, blank=True),
        description=CKEditor5Field(config_name='extends', verbose_name="Описание"),
    )
    category = models.ManyToManyField(Category, null=True, blank=True,
                                      verbose_name='Категория', related_name="category_info")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = TranslatableManager()

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("6. Другая информация об институте")
        verbose_name_plural = _("6. Другая информация об институте")


class AchievementsCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Название категории достижения"), max_length=250, null=True, blank=True),
    )

    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = TranslatableManager()

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("7. Категории достижений")
        verbose_name_plural = _("7. Категории достижений")


class AchievementsQuality(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Название достижения"), max_length=250, null=True, blank=True),
    )
    level = models.CharField(_('Уровень достижений'), null=True, blank=True, max_length=150)
    achievements_category = models.ForeignKey(AchievementsCategory, on_delete=models.CASCADE, null=True, blank=True,
                                              verbose_name="Выберите категорию «Достижения»",
                                              related_name='achievements_category')
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = TranslatableManager()

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True) or 'Безымянный'

    class Meta:
        ordering = ["id"]
        verbose_name = _("8. Достижения Качество")
        verbose_name_plural = _("8. Достижения Качество")