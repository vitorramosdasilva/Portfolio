from django.urls import path
from portfolio.views import IndexView


urlpatterns = [
    path('', IndexView, name='index'),
]