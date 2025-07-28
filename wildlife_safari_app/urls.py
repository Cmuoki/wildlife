from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # Tourist registration and MPESA STK push
    path('register/', views.register_view, name='register'),

    # Payment success page
    path('success/', views.payment_success_view, name='payment_success'),

    # MPESA callback (called by Safaricom API)
    path('api/callback/', views.mpesa_callback, name='mpesa_callback'),
    path('places-to-visit/', views.places_view, name='places'),
]




