from rest_framework import serializers
from .models import Share
from django.conf import settings


MAX_SHARE_LENGTH = settings.MAX_SHARE_LENGTH

class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_SHARE_LENGTH:
            raise serializers.ValidationError("This post is too long")
        return value