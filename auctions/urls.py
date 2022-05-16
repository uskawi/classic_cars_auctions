""" Auctions urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('all_auctions', views.all_auctions, name='all_auctions'),
    path('auction_detail/<int:car_id>/',
         views.auction_detail, name='auction_detail'),
    path('add/', views.add_auction, name='add_auction'),
]
