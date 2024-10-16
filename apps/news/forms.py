from django import forms
from django_select2 import forms as s2forms

from apps.menu.models import Category
from apps.news.models import News
from apps.news.widgets import CategorySelect2Widget


class NewsAdminForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=CategorySelect2Widget,
    )

    class Meta:
        model = News
        fields = '__all__'
