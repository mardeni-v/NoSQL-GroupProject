from django.db import models


class Post(models.Model):
    title = models.CharField(primary_key=True, max_length=1000)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

