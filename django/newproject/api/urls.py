from . import views
from django.urls import path


urlpatterns = [
    path('', views.getData),
    path('add/',views.additem),
]


