from rest_framework import serializers
from .models import Share
from django.conf import settings


MAX_SHARE_LENGTH = settings.MAX_SHARE_LENGTH
SHARE_ACTION_OPTIONS = settings.SHARE_ACTION_OPTIONS


class ShareActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.SerializerMethodField(read_only=True)

    def validate_action(self, value):
        value = value.lower().strip() # "Like" -> "like"
        if not value in SHARE_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for shares")
        return value


class ShareCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Share
        fields = ['id','content', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > MAX_SHARE_LENGTH:
            raise serializers.ValidationError("This post is too long")
        return value

class ShareSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    # content = serializers.SerializerMethodField(read_only=True)
    # is_reshare = serializers.SerializerMethodField(read_only=True)
    parent = ShareCreateSerializer(read_only=True)
    class Meta:
        model = Share
        fields = ['id','content', 'likes', 'is_reshare', 'parent']

    def get_likes(self, obj):
        return obj.likes.count()

    # def get_content(self, obj):
    #     content = obj.content
    #     if obj.is_reshare:
    #         content = obj.parent.content
    #     return content
