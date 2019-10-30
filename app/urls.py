from django.urls import path
from . import views

urlpatterns = [
    path('surveys/', views.surveys, name='surveys'),
    path('survey_form/', views.survey_form, name='survey_form'),
    path('survey/<pk>/', views.survey_detail, name='survey'),
]
