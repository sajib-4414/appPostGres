from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.get_index_page, name='index'),
    url(r'^about/$', views.get_about_page, name='about'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^posts/$', views.all_posts, name='all_posts'),
    url(r'^posts/create$', views.create_new_post, name='create_new_post'),
]