from django.urls import path
from . import views

urlpatterns = [
    path('tanzania/', views.tanzania_escorts, name='tanzania_escorts'),
]
