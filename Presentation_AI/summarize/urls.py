from .views import summarize
from django.urls import path

urlpatterns = [
    path('',summarize,name='Home.html')
]
