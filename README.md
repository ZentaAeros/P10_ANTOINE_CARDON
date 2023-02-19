# Créez une API sécurisée RESTful en utilisant Django REST
Bienvenue dans cette API conçue avec Django Rest Framework !

## Comment executer ce script ?
* Veuillez créer un dossier à l'emplacement souhaité où sera placé le projet.
* Vous pouvez désormais clôner ce dépot dans le dossier fraîchement créé via `git clone https://github.com/ZentaAeros/P10_ANTOINE_CARDON.git`
* Vous pouvez à présent créer un environnement virtuel via : `python -m venv env`
* Activez l'environnement virtuel via `source env/bin/activate`
* Installez les paquets nécessaire à l'éxecution du script à l'aide du fichier *requirements.txt* via `python -m pip install -r requirements.txt`
* Allez à la racine du projet
* Executez la commande python manage.py runserver
* ENJOY ! Vous êtes prêt à utiliser l'application !

## Guide d'utilisation de l'application :
Retrouvez tous les endpoints sur https://documenter.getpostman.com/view/20095524/2s935uGgEt#intro

|   Endpoint   |  Méthode |   Description |
|---           |:-:          |:-:            |
|http://127.0.0.1:8000/api/token/| POST | Permet d'obtenir un token pour accéder à l'application            |
|http://127.0.0.1:8000/api/signup/| POST | Permet de créer un compte pour accéder à l'application            |
|http://127.0.0.1:8000/api/projects/| POST | Permet de créer un projet            |
|http://127.0.0.1:8000/api/projects/| GET | Permet d'obtenir la liste des projets de l'utilisateur            |
|http://127.0.0.1:8000/api/projects/:project_id/| GET | Permet d'obtenir un projet via son ID            |
|http://127.0.0.1:8000/api/projects/:project_id/| PUT | Permet de modifier un projet via son ID            |
|http://127.0.0.1:8000/api/projects/:project_id/| DELETE | Permet de supprimer un projet via son ID            |
|http://127.0.0.1:8000/api/projects/:project_id/issues/| POST | Permet de créer un problème à un projet            |
|http://127.0.0.1:8000/api/projects/:project_id/issues/| GET | Lire un problème d'un projet            |
|http://127.0.0.1:8000/api/projects/:project_id/issues/:issue_id/| PUT | Permet de modifier un problème |
|http://127.0.0.1:8000/api/projects/:project_id/issues/:issue_id/| DELETE | Permet de supprimer un problème           |
|http://127.0.0.1:8000/api/projects/:project_id/issues/:issue_id/comments/| POST | Permet d'ajouter un commentaire            |
|http://127.0.0.1:8000/api/projects/:project_id/issues/:issue_id/comments/| GET | Permet de voir les commentaires            |
|http://127.0.0.1:8000/api/projects/:project_id/issues/:issue_id/comments/:comment_id/| PUT | Permet de modifier un commentaire            |
|http://127.0.0.1:8000/api/projects/:project_id/issues/:issue_id/comments/:comment_id/| DELETE | Permet de supprimer un commentaire            |
|http://127.0.0.1:8000/api/projects/:project_id/issues/:issue_id/comments/:comment_id/| GET | Permet de voir un commentaire via son ID            |
|http://127.0.0.1:8000/api/projects/:project_id/contributors/| POST | Permet d'ajouter un contributeur            |
|http://127.0.0.1:8000/api/projects/:project_id/contributors/| GET | Permet de voir les contributeurs d'un projet            |
|http://127.0.0.1:8000/api/projects/:project_id/contributors/:contributor_id| DELETE | Permet de supprimer un contributeur du projet
