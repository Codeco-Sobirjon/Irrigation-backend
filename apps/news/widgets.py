from django_select2 import forms as s2forms


class CategorySelect2Widget(s2forms.Select2Widget):
    search_fields = ['translations__name__icontains']
    