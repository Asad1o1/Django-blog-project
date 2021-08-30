from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, default='uncategorized')
    snippet = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return str(self.title + '|' + str(self.author))

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')

    def total_like(self):
        return self.likes.count()


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile_pics/")
    linkedin_url = models.CharField(max_length=250, blank=True, null=True)
    instagram_url = models.CharField(max_length=250, blank=True, null=True)
    twitter_url = models.CharField(max_length=250, blank=True, null=True)
    github_url = models.CharField(max_length=250, blank=True, null=True)
    mobile_number = models.CharField(max_length=13, default=9008039697)
    country = models.CharField(max_length=250, default="India")
    state = models.CharField(max_length=250, default="Karnataka")
    city = models.CharField(max_length=250, default="Bangalore")
    postal_code = models.CharField(max_length=13, default=560032)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)