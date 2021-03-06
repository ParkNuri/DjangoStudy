from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:article_pk>/update/', views.update, name="update"),
    path('<int:article_pk>/', views.detail, name="detail"),
    path('<int:article_pk>/delete/', views.delete, name="delete"),
    path('<int:article_pk>/create_comment/', views.create_comment, name="create_comment"),
    path('<int:article_pk>/delete_comment/<int:comment_pk>/', views.delete_comment, name="delete_comment"),
]