from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('resume/', resume, name='resume'),
    path('calories/', calories, name='calories'),
    path('telegram/', telegram, name='telegram'),
    path('contact/', contact, name='contact'),
    path('login/', LoginPage, name = 'login'),
    path('register/', RegisterPage, name='register'),
    path('logout/', LogOutPage, name='logout'),
    path('calories2/<username>/', calories2, name='calories2'),

]
