from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path('index/', views.index, name="index"),
    path('your_champ/', views.your_champ, name="your_champ"),
    path('delete/', views.delete, name="delete"),

]