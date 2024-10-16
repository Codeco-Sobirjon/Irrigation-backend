from django.contrib import admin
from django.contrib.admin.exceptions import NotRegistered
from django.contrib.auth.models import Group
from parler.admin import TranslatableAdmin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from parler.admin import TranslatableTabularInline

from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from apps.main_part.models import (
    AboutInstitution,
    SliderMainPart,
    Partners,
    VideoInstitution,
    Announcement
)


@admin.register(AboutInstitution)
class AboutInstitutionAdmin(TranslatableAdmin):
    list_display = ["name", "year_of_admission", "id", "created_at"]


@admin.register(SliderMainPart)
class SliderMainPartAdmin(TranslatableAdmin):
    list_display = ["title", "slider_image", "id", "created_at"]


@admin.register(Partners)
class PartnersAdmin(TranslatableAdmin):
    list_display = ["name", "id", "created_at"]


@admin.register(VideoInstitution)
class VideoInstitutionAdmin(TranslatableAdmin):
    list_display = ["name", "id", "created_at"]


@admin.register(Announcement)
class AnnouncementAdmin(TranslatableAdmin):
    list_display = ["name", "id", "created_at"]


admin.site.site_header = "Администрирование вашей системы  Tiiamebb.uz"
admin.site.site_title = "Панель администратора Tiiamebb.uz"
admin.site.index_title = "Добро пожаловать в панель администратора Tiiamebb.uz"

