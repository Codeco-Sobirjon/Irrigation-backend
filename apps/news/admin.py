from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.utils.translation import gettext_lazy as _

from apps.news.forms import NewsAdminForm
from apps.news.models import (
    News,
    NewsImages,
    Comment,
    Postions, Staffs, ContactInfo,
    InfoAboutInstitution,
    AchievementsCategory,
    AchievementsQuality
)
from apps.menu.models import (
    Category, SubCategory,
    TopLevelCategory, TertiaryCategory
)
from apps.news.utils import image_preview


class TopLevelCategoryFilter(admin.SimpleListFilter):
    title = _('Основная категория')
    parameter_name = 'top_level_category'

    def lookups(self, request, model_admin):
        categories = Category.objects.filter(parent__isnull=True)
        return [(category.id, category.safe_translation_getter('name')) for category in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset


class SubCategoryFilter(admin.SimpleListFilter):
    title = _('Подкатегория')
    parameter_name = 'sub_category'

    def lookups(self, request, model_admin):
        categories = Category.objects.filter(parent__isnull=False, parent__parent__isnull=True)
        return [(category.id, category.safe_translation_getter('name')) for category in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset


class TertiaryCategoryFilter(admin.SimpleListFilter):
    title = _('Третичная категория')
    parameter_name = 'tertiary_category'

    def lookups(self, request, model_admin):
        categories = Category.objects.filter(parent__isnull=False, parent__parent__isnull=False)
        return [(category.id, category.safe_translation_getter('name')) for category in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())
        return queryset


class CategoryFilter(admin.SimpleListFilter):
    title = 'category'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        categories = Category.objects.all()
        return [(cat.id, cat.__str__()) for cat in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(categories__id=self.value())
        return queryset


class NewsImagesInline(admin.TabularInline):
    model = NewsImages
    extra = 1
    fields = ['image']
    readonly_fields = ['_image']

    def _image(self, obj):
        image = obj.image
        return image_preview(image, height=100, width=100)

    _image.short_description = ''


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = ('title', 'viewers', 'created_at', 'id')
    search_fields = ('translations__title', 'categories__translations__name')
    inlines = [NewsImagesInline]
    readonly_fields = ('created_at',)
    list_filter = (TopLevelCategoryFilter, SubCategoryFilter, TertiaryCategoryFilter, CategoryFilter)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_moderator', 'created_at', 'news', 'id')
    search_fields = ('full_name',)
    readonly_fields = ('created_at',)


@admin.register(Postions)
class CommentAdmin(TranslatableAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)


@admin.register(Staffs)
class CommentAdmin(TranslatableAdmin):
    list_display = ('full_name', 'position', 'created_at', 'id')
    search_fields = ('full_name',)
    readonly_fields = ('created_at',)


@admin.register(ContactInfo)
class CommentAdmin(TranslatableAdmin):
    list_display = ('adress', 'comapany_phone', 'created_at', 'id')
    readonly_fields = ('created_at',)


@admin.register(InfoAboutInstitution)
class CommentAdmin(TranslatableAdmin):
    list_display = ('title', 'created_at', 'id')
    readonly_fields = ('created_at',)


@admin.register(AchievementsCategory)
class CommentAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'id')
    readonly_fields = ('created_at',)


@admin.register(AchievementsQuality)
class CommentAdmin(TranslatableAdmin):
    list_display = ('title', 'level', 'created_at', 'id')
    readonly_fields = ('created_at',)
