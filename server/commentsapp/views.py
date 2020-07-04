from django.shortcuts import render
from django.shortcuts import get_object_or_404
import random
from rest_framework import status
from rest_framework import serializers
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import CommentsSerializer
from .models import Comments

# Create your views here.

def TotalCommentList(request):
    comment_list = Comments.objects.all()
    serializer = CommentsSerializer(comment_list, many=True)
    return JsonResponse(serializer.data, safe=False)


class Insert(generics.ListCreateAPIView):

    queryset = Comments.objects.all()

    serializer_class = CommentsSerializer

def CommentListRefined(request, top):
    comment_list = Comments.objects.filter(Q(Topic=top)).distinct()
    serializer = CommentsSerializer(comment_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def GetListOfTopics(request):
    comment_list = Comments.objects.all()
    topics = []
    for comment in comment_list:
        if comment.Topic in topics:
            continue
        else:
            topics.append(comment.Topic)
    context = {
        'ListOfTopics': topics
    }
    return JsonResponse(context,safe=False)

class InsertDetail(APIView):
    def get(self, request, pk):
        comment = get_object_or_404(Comments, commentId=pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, pk):
        comment = get_object_or_404(Comments, commentId=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
