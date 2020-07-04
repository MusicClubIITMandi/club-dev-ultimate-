from django.urls import path

from django.contrib import admin

from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('recommendation/', views.RecommendationList.as_view(),
         name='recommendations'),
    path('<str:payload>/',
         views.Get3Recommendations, name='recommendations'),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
