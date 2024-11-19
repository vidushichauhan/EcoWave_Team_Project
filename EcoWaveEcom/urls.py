from django.urls import path
from . import views

app_name = 'EcoWave'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('eco_guides/', views.eco_guide, name='eco_guide'),
    path('ecofriendly_tips/', views.ecofriendly_tips, name='ecofriendly_tips'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unverified-products/', views.unverified_products, name='unverified_products'),
    
]