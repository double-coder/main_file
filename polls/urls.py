from django.conf.urls import url

from . import views

urlpatterns = [
   # url(r'^', views.index, name='index'),
     url(r'^$', views.polls_req, name='polls_req'),
]
