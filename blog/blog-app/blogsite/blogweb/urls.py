from django.urls import path
from blogweb.views import *

urlpatterns = [
    path('',home, name='index'),
    path('about',about, name='about'),
    path('<int:id>',postDetail,name='post-detail'),
    path('new-comment',addComment, name='add-comment'),
    path('add-post', addPostView.as_view(), name='add-post'),
    path('author-list', authors, name='author-list'),
]
