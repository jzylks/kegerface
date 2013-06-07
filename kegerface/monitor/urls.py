from django.conf.urls import patterns, include, url

from .views import TapListView

urlpatterns = patterns('',
    url(r'^$', TapListView.as_view(), name='tap-list'),
)
