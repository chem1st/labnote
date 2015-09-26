from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles import views
from core.views import SynthesisList, SynthesisDetail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', SynthesisList.as_view(), name='synths'),
    url(r'^synthesis/(?P<pk>[0-9]+)/$', SynthesisDetail.as_view(), name='synthesis'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', views.serve),
    ]