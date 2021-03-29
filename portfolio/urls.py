from django.urls import path
from portfolio.views import indexView


urlpatterns = [
    path('', indexView, name='index'),
]