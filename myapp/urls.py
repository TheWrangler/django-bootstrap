 #from django.conf.urls import urls
from django.urls import path
from . import views
 
app_name='myapp'
 
urlpatterns = [
    path('',views.index,name='index'),
     ]
