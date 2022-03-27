## LITReview

## Installation
* Python 3 doit-etre installé.
* Télécharger le package de l'application sous github, le dézipper et le ranger dans un nouveau répertoire.
* Sous windows ouvrir un terminal avec la commande cmd depuis ce répertoire.
* Créer un environnement virtuel `python -m venv env`
* Activer l'environnement virtuel `./env/Scripts/activate.bat`
* Installer les bibliothèques externes de Python `pip install -r requirements.txt`

_**L'application est développée avec Django. Le projet Django litreview a trois applications:**_
1. authentication
2. flux
3. follow

_**Les données sont sauvées dans la base de données db.sqlite3**_

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

_**Liste des autres utilisateurs de demonstration déjà créés:**_
* MattGris
* Pierre
* toto
* EloCot

_**Le mot de passe est toujours OcR2022!**_

### Fonctionnalités
Une fois connecté, la barre de navigation en haut à droite permet d'accéder aux différentes fonctionnalités de l'application

_**Flux**
Page d'accueil, vous trouverez ici les tickets et critiques que vous postez ou que vos amis postent, et les réponses à vos tickets.
C'est ici que vous pouvez créer de nouveaux tickets ou de nouvelles critiques, ou encore de répondre à des tickets.

_**Posts**
Vous trouverez sur cette page tous vos posts et pourrez les modifier ou les supprimer.

_**Abonnements**
Gérez ici les abonnements aux autres utilisateurs: visualisez qui vous suit et qui vous suivez déjà.

## Vérification du code

Pour vérifier la conformité du code et générer un rapport flake8, vous pouvez lancer le script ctrl_flake8.py:

```sh
python ctrl_flake8.py
```