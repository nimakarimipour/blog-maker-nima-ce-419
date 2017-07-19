from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.sign_in, name='sign_in'),
    url(r'^register/', views.sign_up, name='sign_up'),
    url(r'^blog_id/', views.get_home_blog_id, name='get_home_blog_id'),
    url(r'^test/', views.test, name='test'),
]
