from django.urls import path

from . import views

urlpatterns = [
    path('pricing', views.pricing, name='pricing'),
    path('thanks/', views.add_faq, name='add_faq'),
    path('', views.homepage, name='homepage'),
]