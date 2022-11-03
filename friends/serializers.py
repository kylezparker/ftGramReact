from rest_framework import serializers
from .models import Share
from django.conf import settings


MAX_SHARE_LENGTH = settings.MAX_SHARE_LENGTH
SHARE_ACTION_OPTIONS = settings.SHARE_ACTION_OPTIONS


class ShareActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip() # "Like" -> "like"
        if not value in SHARE_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for shares")
        return value

class ShareSerializer(serializers.ModelSerializer):
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