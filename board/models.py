from django.db import models


class Post(models.Model):
    date_posted = models.DateTimeField("date posted")
    name = models.CharField(max_length=255, blank=True, default='Anonymous')
    image_url = models.CharField(max_length=1024, blank=True, default='')
    post_text = models.CharField(max_length=1024)


class Thread(Post):
    title = models.CharField(max_length=255, blank=True, default='')


class Reply(Post):
    corresponding_thread = models.ForeignKey(
        Thread, related_name="replies", on_delete=models.CASCADE)
