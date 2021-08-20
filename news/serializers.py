from rest_framework import serializers

from news.models import Author, Notice


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(required=True, source='author', write_only=True)
    author = AuthorSerializer(required=False, allow_null=True)

    class Meta:
        model = Notice
        fields = ['id', 'title', 'notice', 'author_id', 'author', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def validate_author_id(self, value):
        try:
            return Author.objects.get(pk=value)
        except Author.DoesNotExist:
            raise serializers.ValidationError('Author not found')
