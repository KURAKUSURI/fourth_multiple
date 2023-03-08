from app2.views import *

from django.urls import path

add_name = 'nothing'

urlpatterns = [
     path('virat/',virat,name='virat'),
     path('ABD/',ABD,name='ABD'),
]