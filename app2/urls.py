from django.urls import path
from app2.views  import *
app_name="first"
urlpatterns=[
    path('itishree/',itishree,name='itishree')
]