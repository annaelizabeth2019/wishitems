from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.ItemCreate.as_view(), name='form'),
    path('<int:pk>/delete/', views.ItemDelete.as_view(), name='delete')
]