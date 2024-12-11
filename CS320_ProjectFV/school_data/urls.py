

# school_data/urls.py
from django.urls import path
from . import views


urlpatterns = [
    # path('schools/', views.school_list, name='school_list'),
    # path('schools/create/', views.create_school, name='create_school'),
    # path('schools/update/<int:schl>/', views.update_school, name='update_school'),
    # path('schools/delete/<int:schl>/', views.delete_school, name='delete_school'),
    #  path('schools/<int:schl>/', views.school_detail, name='school_detail'),
    path('schools/low-income-histogram/', views.low_income_histogram, name='low_income_histogram'),
    path('schools/test-scores-histogram/', views.test_scores_histogram, name='test_scores_histogram'),
    path('', views.index, name='index'),
    path('school/list/', views.school_list, name='school_list'),
    path('school/<int:pk>/', views.school_detail, name='school_detail'),
    path('school/new/', views.school_create, name='school_create'),
    path('school/<int:pk>/edit/', views.school_update, name='school_update'),
    path('school/<int:pk>/delete/', views.school_delete, name='school_delete'),
    path('school/comparison/', views.school_comparison, name='school_comparison'),
    path('get-counties/<str:district>/', views.get_counties, name='get_counties'),
    path('get-schools/<str:district>/<str:county>/', views.get_schools, name='get_schools'),
    path('school/regions/', views.region_comparison, name='region_comparison'),
    path('school/search_school', views.search_school, name='search_school')
]
