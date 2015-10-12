from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^top-20', views.top_20, name='top_20'),

]
