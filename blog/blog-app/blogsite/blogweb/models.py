from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    biography = models.TextField(max_length=2000, help_text="Enter your biography details here.")


    class Meta:
        ordering = ["user","biography"]

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user.username


class blogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")

    class Meta:
        ordering = ["-publish_date"]

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class comment(models.Model):
    blog = models.ForeignKey(blogPost, related_name="comments",on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["publish_date"]

    def __str__(self):
        return f'{self.author}: {self.description}'
