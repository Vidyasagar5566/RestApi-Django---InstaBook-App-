from django.urls import path
from . import views

urlpatterns = [

    path('test_api3', views.testing_api3.as_view(),name = 'testing_api3'),
]