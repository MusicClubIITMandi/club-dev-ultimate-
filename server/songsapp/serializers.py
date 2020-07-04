from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Recommendation


class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'
