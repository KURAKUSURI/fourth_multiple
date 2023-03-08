from app1.views import *

from django.urls import path

add_name='nothing'

urlpatterns = [
    path('dhoni/',dhoni,name='dhoni'),
    path('raina/',raina,name='raina'),
    
]

