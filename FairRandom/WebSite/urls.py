from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('share/<str:url>', views.choose_time, name='choose_time'),
]

