from urllib.parse import urlparse
import django


from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.passwordgen, name='password'),
    path('yourpass/',views.yourpass, name='yourpass'),
    path('about/',views.about, name = 'about')
]
