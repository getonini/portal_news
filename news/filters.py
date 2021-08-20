# -*- coding: utf-8 -*-

from django_filters import FilterSet, DateFilter, CharFilter

from news.models import Notice


class NoticeFilter(FilterSet):
    created_at_start = DateFilter(field_name='created_at__date', lookup_expr='gte')
    created_at_end = DateFilter(field_name='created_at__date', lookup_expr='lte')
    title = CharFilter(lookup_expr='icontains')
    notice = CharFilter(lookup_expr='icontains')
    author_name = CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Notice
        fields = ['title', 'notice', 'author_name']
