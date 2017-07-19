from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<blog_id>[0-9]+)/posts/', views.get_posts, name='get_posts'),
    url(r'^(?P<blog_id>[0-9]+)/post/', views.get_post, name='get_post'),
    url(r'^comments/', views.get_comments, name='get_comments'),
    url(r'^comment/', views.add_comment, name='add_comments'),
]