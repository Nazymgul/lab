from operator import index
from django.urls import path

from .views import *

urlpatterns = [
    path('additionalpage/', additionalpage, name='additional_page'),
    path('index/', index, name='index'),
    path('send/', send_message)
]