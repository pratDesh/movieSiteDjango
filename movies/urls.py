from django.conf.urls import url
from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('<int:num>',views.index , name='Index'),
    path('dets/<str:nam>',views.info,name='details')
    #(r'^movie_detail/(?P<id>.*)'
    #path('homePage/<str:movieName1>/',views.details,name='details'),
]