from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("<int:listas_id>", views.listas, name="listas")

]