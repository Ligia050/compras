from django.urls import path 
from . import views

app_name ="listas"
urlpatterns = [
    path("", views.index, name ="index"),
    path("<int:id>", views.listas, name="listas"),
   
]