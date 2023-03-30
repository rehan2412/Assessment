from django.urls import path
from Projectapp.views import AccountAPI,AccountRegister,DestinationAPI
  
urlpatterns = [
    path('register', AccountRegister.as_view()),
    path('account', AccountAPI.as_view()),
    path('destination', DestinationAPI.as_view()),  
]  