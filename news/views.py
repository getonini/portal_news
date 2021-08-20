from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from news.filters import NoticeFilter
from news.models import Notice, Author
from news.serializers import NoticeSerializer, AuthorSerializer

__author__ = 'Guilherme Tonini'


class NoticeViewSet(viewsets.ModelViewSet):

    serializer_class = NoticeSerializer
    filter_class = NoticeFilter
    search_fields = ('title', 'notice', 'author_name')
    ordering = ('id',)

    def get_queryset(self):
        return Notice.objects.all()

    def list(self, request, *args, **kwargs):
        qset = self.filter_class(request.query_params, queryset=self.get_queryset()).qs
        serializer = self.get_serializer(qset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class AuthorViewSet(viewsets.ModelViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):

    serializer_class = AuthorSerializer
    ordering = ('id',)

    def get_queryset(self):
        return Author.objects.all()
