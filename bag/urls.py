""" Won_Auctions urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag')
]