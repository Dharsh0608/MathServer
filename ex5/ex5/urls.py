from django.contrib import admin 
from django.urls import path 
from design import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('power/',views.power,name="power"),
    path('',views.power,name="power")
]