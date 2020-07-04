from django.urls import path

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib import admin

urlpatterns = [
    path('', views.TotalCommentList, name='List1'),
    path('get/<str:top>/', views.CommentListRefined, name='List2'),
    path('gettopics/', views.GetListOfTopics, name="topics"),
    path('addcomment/', views.Insert.as_view()),
    path('delete/<int:pk>/', views.InsertDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)