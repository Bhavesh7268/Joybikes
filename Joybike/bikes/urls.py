from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('bike/<int:pk>/', views.bike_detail, name='bike_detail'),
    path('accounts/', include('allauth.urls')),
    
]