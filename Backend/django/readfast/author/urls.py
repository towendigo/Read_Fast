from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.GetAll),
    path('id=<int:author_id>/', views.GetById),
    path('name=<slug:author_name>/', views.GetByName),

    path('<str:lan>/all', views.GetAll),
    path('<str:lan>/id=<int:author_id>/', views.GetById),
    path('<str:lan>/name=<slug:author_name>/', views.GetByName),
]
