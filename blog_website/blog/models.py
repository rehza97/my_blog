from django.db import models
from user_profile.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True,unique=True,blank=True )
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(null=True,unique=True,blank=True)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Blog(models.Model):
    user = models.ForeignKey(User , related_name='user_blog', on_delete=models.CASCADE)
    category = models.ForeignKey(Category ,related_name='category_blog', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag ,related_name='tag_blog' ,blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True,unique=True,blank=True)
    banner = models.ImageField(upload_to='blog_banner' , blank=True)
    like = models.ManyToManyField(User , related_name='user_like')
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
class Comment(models.Model):
    user = models.ForeignKey(User , related_name='user_comment', on_delete=models.CASCADE)
    blog = models.ForeignKey('Blog', related_name='blog_comment', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f' {self.text[:30]} by {self.user.username} on {self.blog.title}:'
    
class Replay(models.Model):
    user = models.ForeignKey(User , related_name='user_comment_replay', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='blog_comment_replay', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f' {self.text[:30]}  {self.user.username} replay to {self.comment.user.username}'
