from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    """ A serializer for the Comments model """
    class Meta:
        model = Comments
        fields = ('commentId','Time', 'Topic','DisplayName', 'Author', 'Comment')