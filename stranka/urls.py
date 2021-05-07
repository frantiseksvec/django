from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('vypis', views.StrojList.as_view(),name='vypis'),
    path('detail/<int:pk>/', views.DetailStroj.as_view(),name='detail'),
]