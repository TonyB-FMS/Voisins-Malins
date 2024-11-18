from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Affiche la page d'accueil
    path('signup/', views.signup, name='signup'),  # Page d'inscription
    path('login/', views.login, name='login'),  # Page de connexion
]
