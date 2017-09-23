from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.tagpage,name="tagpage"),
    url(r'^tag/(?P<slug>[\w\-]+)/$',views.quotepage,name="quotepage"),
    url(r'^person/$',views.personpage,name="personpage"),
    url(r'^quotes/(?P<slug>[\w\-]+)/$',views.personquotes,name="personquotes"),
    url(r'^check/$',views.check,name="check"),
]