from django.urls import path
from . import views

# This variable name MUST be exactly 'urlpatterns'
urlpatterns =[
    path('addTask/', views.addTask, name='addTask'),
    path("mark_as_done/<int:pk>/",views.mrk_as_done, name="mrk_as_done"),

    path('edit/<int:pk>/', views.edit,name='edit'),
    path('delete/<int:pk>/', views.delete,name='delete')
]