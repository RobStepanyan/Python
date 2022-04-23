from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_items),
    path('create/', views.create_items),
]
