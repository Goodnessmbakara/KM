from django.urls import path
from apps.portfolio.views import *



urlpatterns = [
    path('portfolios/<slug:slug>/', PortfolioListView.as_view(), name='portfolio_list'),
    #path('categories/<slug:category_slug>/', PortfolioListView.as_view(), name='portfolio_list'),
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]
