from django.urls import path
from . import views

# This variable name MUST be exactly 'urlpatterns'
urlpatterns =[
    path('addTask/', views.addTask, name='addTask'),
]