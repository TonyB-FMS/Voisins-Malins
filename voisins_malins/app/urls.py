from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Affiche la page d'accueil
    path('signup/', views.signup_view, name='signup'),  # Page d'inscription
    path('login/', views.login_view, name='login'),  # Page de connexion
]
