from django.db import models


class Post(models.Model):
    date_posted = models.DateTimeField("date posted")
    name = models.CharField(max_length=255, blank=True, default='Anonymous')
    image_url = models.CharField(max_length=1024, blank=True, default='')
    post_text = models.CharField(max_length=1024)


class Thread(Post):
    title = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        parts = [
            str(super().id),
            str(super().date_posted),
            str(self.title),
            str(super().name),
            str(super().post_text),
        ]

        return "-".join(p for p in parts if p)


class Reply(Post):
    corresponding_thread = models.ForeignKey(
        Thread, related_name="replies", on_delete=models.CASCADE)

    def __str__(self):
        parts = [
            str(super().id),
            str(super().date_posted),
            "thread id:" + str(self.corresponding_thread.id),
            str(super().name),
            str(super().post_text),
        ]

        return "-".join(p for p in parts if p)
        """
        return str(super().id) + str(super().date_posted) + \
            str(self.corresponding_thread.super().id) + \
            str(super().name) + str(super().post_text)
        """
