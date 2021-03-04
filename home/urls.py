from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("",views.index, name = 'Home'),
    path("about",views.about, name = 'about'),
     path("services",views.services, name = 'services'),
      path("contact",views.contact, name = 'contact'),
       #path("submit contact",views.contact, name = 'contact'),
    #path('admin/', admin.site.urls),
   # path('',include('home.urls'))
]