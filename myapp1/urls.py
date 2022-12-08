from django.urls import path
from . import views

urlpatterns=[
    path('myurl/',views.fun1,name="1sturl"),
    path('myurl2/',views.fun2,name="url2")
]