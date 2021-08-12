from django.urls import path
from .views import home, user_sign_up
 
urlpatterns = [
    path('', home, name='home'),
    path('signup/', user_sign_up, name='signup' ),
]