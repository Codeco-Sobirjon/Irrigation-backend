from django_filters import FilterSet, NumberFilter, CharFilter
from django.db.models import Q
from django_filters import rest_framework as filters
from apps.news.models import News


class NewsFilterSet(FilterSet):
    category = NumberFilter(field_name='category', lookup_expr='id')
    title = CharFilter(field_name='translations__title', lookup_expr='icontains')
    is_three_menu_news = filters.BooleanFilter(method='filter_three_menu_news')
    is_four_menu_news = filters.BooleanFilter(method='filter_four_menu_news')

    class Meta:
        model = News
        fields = ['category', 'title']

    def filter_three_menu_news(self, queryset, name, value):
        if value:
            return queryset.order_by('-created_at')[:3]
        return queryset

    def filter_four_menu_news(self, queryset, name, value):
        if value:
            return queryset.order_by('-created_at')[3:7]
        return queryset
