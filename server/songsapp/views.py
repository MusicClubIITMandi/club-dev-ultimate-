from django.shortcuts import render
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recommendation
from .serializers import RecommendationsSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


@api_view(('GET',))
def Get3Recommendations(self, payload):

    all_songs = Recommendation.objects.filter(
        recommendation_song_genre=payload).distinct()

    three_songs = random.sample(list(all_songs), 3)
    serializer = RecommendationsSerializer(three_songs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class RecommendationList (APIView):

    def get(self, request):
        all_songs = Recommendation.objects.all()
        serializer = RecommendationsSerializer(all_songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RecommendationsSerializer(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
