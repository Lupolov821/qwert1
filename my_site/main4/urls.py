from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.index),
    path('page1.html',views.page1),
    path('page2.html',views.page2),
    path('page3.html',views.page3),
    path('page4.html',views.page4)
]
