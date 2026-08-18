from django.urls import path
from .views import reporters_view, issues_view

urlpatterns = [
    path('reporters/', reporters_view, name='reporters'),
    path('issues/', issues_view, name='issues'),
]

