from django.urls import path
from .views import *

urlpatterns = [
    path('',home ,name='home'),
    path('blogs/',blogs ,name='blogs'),
    path('categories/<str:slug>',category_blogs ,name='categories'),
    path('tags/<str:slug>',tag_blogs ,name='tags_blogs'),
    path('post/<str:slug>',post_details ,name='post_details'),
]