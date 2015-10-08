from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/top', views.top_20)
]
