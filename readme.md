_**LITReview**_

_**L'application est développée avec Django. Le projet Django litreview a trois applications:**_
1. authentication
2. flux
3. follow

_**Les données sont sauvées dans la base de données db.sqlite3**_

## Installation
* Python 3 doit-etre installé.
* Télécharger le package de l'application sous github, le dézipper et le ranger dans un nouveau répertoire.
* Sous windows 10 ouvrir un terminal avec la commande cmd depuis ce répertoire.
* Créer un environnement virtuel `python -m venv env`
* Activer l'environnement virtuel `env\Scripts\activate.bat`
* Installer les bibliothèques externes de Python `pip install -r requirements.txt`

## Utilisation
* Activer l'environnement virtuel `env\Scripts\activate.bat`
* Lancer le serveur avec la commande `python manage.py runserver`
* Dans votre navigateur, accéder à l'application à l'adresse `http:/127.0.0.1:8000`
* Créer un compte ou se connecter pour pouvoir accéder au site.
* Pour accéder à l'administratin de django `http://127.0.0.1:8000/admin`
>Nom d’utilisateur : Matthieu
>
>Mot de passe : OcR2022!
>
* Pour créer un nouvel administrateur dans le terminal `python manage.py createsuperuser`