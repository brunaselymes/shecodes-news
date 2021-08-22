from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.CharField(
        max_length=140, default='')

    class Meta:
        ordering = ['pub_date']


class RecentUpdate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    image_url = models.CharField(
        max_length=140, default='')

    def __str__(self):
        return self.title
