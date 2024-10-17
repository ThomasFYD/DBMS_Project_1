

# school_data/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('schools/', views.school_list, name='school_list'),
    path('schools/create/', views.create_school, name='create_school'),
    path('schools/update/<int:schl>/', views.update_school, name='update_school'),
    path('schools/delete/<int:schl>/', views.delete_school, name='delete_school'),
    path('schools/<int:schl>/', views.school_detail, name='school_detail'),  # Detail view
]
