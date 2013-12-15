from django.conf.urls import patterns, url

from showTweets import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)