from django.db import models
from user_profile.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True , null=True)
    created_date = models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title
    
class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True , null=True)
    created_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_comment')
    
    def __str__(self):
        pass

    
class Blog(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_blogs')
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='category_blog')
    tags = models.ManyToManyField(Tags , related_name='tag_blog' , blank=True)
    title = models.CharField(max_length=200)
    comments = models
    banner = models.ImageField(upload_to='blog_banners')
    slug = models.SlugField(blank=True , null=True)
    created_date = models.DateField(auto_now_add=True)
    desc = models.TextField()
    def __str__(self) -> str:
        return self.title
    
    