# Voisins Malins

Voisins Malins est une application Web permettant à des utilisateurs d'échanger des compétences et d'accomplir des activités à travers des créneaux horaires convenus, dans le but d'aider d'autres utilisateurs en fonction de leurs compétences et disponibilités.


## Fonctionnalités

#### Visiteurs :

- Visualiser les compétences proposées par les utilisateurs.
- Voir les créneaux où des utilisateurs sont disponibles pour aider avec leurs compétences.

#### Utilisateurs connectés :

Indiquer les compétences qu'ils possèdent et sont prêts à offrir.
Définir des créneaux où ils sont disponibles pour aider.
Rechercher des créneaux où un autre utilisateur a besoin d'aide dans une activité où l'utilisateur n'a pas la compétence nécessaire.
Visualiser les créneaux où un autre utilisateur propose de l'aide.
Prendre un créneau disponible pour aider une autre personne.


## Technologies utilisées

Django 4.2.16 : Framework Web Python pour le développement de l'application.
SQLite : Base de données par défaut pour le stockage des données.
HTML/CSS : Frontend pour l'interface utilisateur.
Git : Gestionnaire de version pour suivre les changements du projet.


## Installation

#### Prérequis

Avant de démarrer, assurez-vous d'avoir installé Python et Django. Vous pouvez vérifier si Python est installé avec la commande suivante :

python --version

Installez Django avec pip :

pip install django==4.2.16


#### Clonez le dépôt

Clonez ce projet sur votre machine locale avec Git :


git clone https://github.com/votre-utilisateur/voisins-malins.git
cd voisins-malins


## Configuration de la base de données

Ce projet utilise SQLite par défaut, donc aucune configuration supplémentaire de base de données n'est nécessaire. Vous pouvez maintenant créer les tables et effectuer les migrations en exécutant les commandes suivantes :


python manage.py migrate
Démarrer le serveur
Lancez le serveur de développement pour voir l'application en action :

_python manage.py runserver_
Accédez ensuite à http://127.0.0.1:8000/ dans votre navigateur pour voir l'application.

## Identifiants des comptes utilisateur
- admin / fmsfmsfms

## Structure du projet

Voici un aperçu des dossiers et fichiers principaux du projet :


voisins_malins/
├── voisins_malins/
│   ├── __init__.py
│   ├── settings.py         # Paramètres du projet Django
│   ├── urls.py             # URLs du projet
│   ├── wsgi.py             # Point d'entrée WSGI
├── app/
│   ├── __init__.py
│   ├── admin.py            # Interface d'administration Django
│   ├── models.py           # Définition des modèles de la base de données
│   ├── views.py            # Vues de l'application
│   ├── urls.py             # Routes spécifiques à l'application
│   ├── templates/          # Templates HTML
│   ├── static/             # Fichiers CSS, JS, images
├── db.sqlite3              # Base de données SQLite
├── manage.py               # Script principal pour gérer Django


## Test

Des tests unitaires sont inclus dans le fichier app/tests.py. Vous pouvez les exécuter avec la commande suivante :


_python manage.py test_
Cela vérifiera que les principales fonctionnalités du projet fonctionnent comme prévu.