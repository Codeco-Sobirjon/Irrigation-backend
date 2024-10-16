from django.contrib import admin
from parler.admin import TranslatableAdmin
from apps.menu.models import (
    Category,
    TopLevelCategory,
    SubCategory,
    TertiaryCategory
)


# Admin for top-level categories (Categories without parents)
class TopLevelCategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'created_at', 'id')
    search_fields = ('translations__name',)
    list_filter = ('created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=True)

    def name(self, obj):
        return obj.safe_translation_getter('name', any_language=True) or 'Безымянный'

    name.short_description = 'Название категория'

    # Override get_form to exclude the parent field
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None or obj.parent is None:
            form.base_fields.pop('parent', None)  # Remove the 'parent' field for top-level categories
        return form


# Admin for subcategories (Categories with a parent but no sub-subcategories)
class SubCategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'parent', 'created_at', 'id')
    search_fields = ('translations__name', 'parent__translations__name')
    list_filter = ('parent', 'created_at')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=False, parent__parent__isnull=True)

    def name(self, obj):
        return obj.safe_translation_getter('name', any_language=True) or 'Безымянный'

    name.short_description = 'Название подкатегория'

    # Filter parent field to show only top-level categories (categories without parents)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            kwargs['queryset'] = Category.objects.filter(parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Admin for tertiary categories (Categories with a parent that is a subcategory)
class TertiaryCategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'parent', 'created_at', 'id')
    search_fields = ('translations__name', 'parent__translations__name')
    list_filter = ('parent', 'created_at')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=False, parent__parent__isnull=False)

    def name(self, obj):
        return obj.safe_translation_getter('name', any_language=True) or 'Безымянный'

    name.short_description = 'Название тертиарной категории'

    # Filter parent field to show only subcategories (categories that have a parent but are not tertiary)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'parent':
            kwargs['queryset'] = Category.objects.filter(parent__isnull=False, parent__parent__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Register separate admin panels for each category level
admin.site.register(TopLevelCategory, TopLevelCategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(TertiaryCategory, TertiaryCategoryAdmin)