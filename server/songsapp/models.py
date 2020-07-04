from django.db import models


class Recommendation(models.Model):
    recommendation_song_name = models.CharField(
        max_length=30, primary_key=True)
    recommendation_song_artist = models.CharField(max_length=30)
    recommendation_song_genre = models.CharField(max_length=30)
