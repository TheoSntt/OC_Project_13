# Orange County Lettings

## Présentation du projet

Il s'agit du dernier projet de ma formation de Développeur Python sur OpenClassrooms. Le site "Orange County Lettings", aux fonctionnalités très limitées, n'est que la base de travail du projet.  
L'enjeu du projet était d'apporter un certain nombre d'amélioration au [site de base](https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR).  
Dans un premier temps, il fallait modulariser l'architecture du site en créant de nouvelles apps Django et en y déplaçant les modèles, vues et URL, qui se trouvaient tous dans une seule application monolithique. Cette étape m'a permis d'approfondir ma connaissance des migrations Django, car il fallait déplacer les modèles sans perdre les données.  
Ensuite, il fallait corriger un certain nombre d'erreurs, mettre en place des tests (avec une couverture de tests de plus de 80%), et mettre en place une surveillance à l'aide de Sentry.  
La création d'une documentation en ligne à l'aide de Sphinx et Readthedocs était aussi demandé, ce qui m'a permis de me familiariser avec ces outils.  
Enfin, la partie la plus importante du projet consistait en la mise en place d'un pipeline CI/CD, à l'aide de CircleCI. Cela m'a poussé à me familiariser avec de nombreux nouveaux outils : CircleCI évidemment, mais aussi Docker, Dockerhub, Render, ou même whitenoise pour la gestion des fichiers statiques dans une application Django déployée.

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
- Compte Sentry

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/TheoSntt/oc-lettings.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Créer les variables d'environnement

- Ajouter une variable `OC_LETTINGS_DJANGO_SECRET_KEY` à vos variables d'environnement.
  Pour la version de développement, la clé est `fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s`
- Ajouter une variable `OC_LETTINGS_SENTRY_DNS` à vos variables d'environnement.
  Renseignez la valeur fournie par Sentry lors de la création de l'application sur votre compte.

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8` pour simplement exécuter le linting
- ou `flake8 --format=html --htmldir=rapport` pour générer un rapport recensant toutes les erreurs de linting.

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest` pour simplement exécuter la suite de tests unitaires
- ou `pytest --cov=. --cov-report html` pour générer un rapport sur la couverture de test.

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `SELECT user_id, favorite_city FROM
  profiles_profile WHERE favorite_city LIKE 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

---
## Déploiement

**Pré-requis :**

- Un compte/Accès Github
- Un compte/Accès CircleCI
- Un Compte/Accès DockerHub
- Un Compte/Accès Render
- Un Compte/Accès Sentry

### Fonctionnement du Pipeline CircleCI

Le fonctionnement du pipeline CircleCI est défini au sein du fichier .circleci/config.yml

#### Lorsqu'un commit est push sur n'importe quelle branche du repository distant (GitHub) :
- Le job 'unit-tests-and-linter' s'éxécute.
  - Il se compose de 3 étapes :
    - Linter : 
      - exécute le linting à l'aide de flake8
    - Run Tests :
      - exécute la suite de tests unitaires à l'aide de pytest et calcule la couverture de test (la pipeline échoue -et le commit n'est pas push- si un test échoue)
    - Check Test Coverage
      - Vérifie que la couverture de test est supérieure à 80% (la pipeline échoue -et le commit n'est pas push- si ce n'est pas le cas)
    
#### Lorsqu'un commit est push sur la branche main du repository distant (GitHub) :
   
- Le job 'unit-tests-and-linter' s'éxécute, dans les mêmes conditions que celles décrites dans la section précédentes.
- Une fois ce job terminé et réussi, le job 'build-push-docker' s'éxécute.
  - Il se compose de 2 étapes :
    - Build Docker image
      - Construit une image Docker du site sur la base du fichier Dockerfile contenu dans à la racine du projet
    - Push Docker image
      - Publie l'image sur le DockerHub. L'image est push 2 fois, avec 2 tags différents : le hash du commit d'une part, et 'latest' d'autre part. Cela permet de récupérer facilement la dernière image depuis le DockerHub, sans avoir à connaître le hash du dernier commit.
- Une fois ce job terminé et réussi, le job 'deploy-to-render' s'exécute.
  - Ce job est en une seule étape :
    - Deploy:
      - Utilise le 'deploy hook' fourni par Render lors de la création de l'application sur la plateforme afin de déployer le site sur Render.

---

## CircleCi :

Paramétrage nécessaire : 

Création des variables d'environnement au niveau du projet :

- Dans **Projets**:
- Cliquez sur `Project Settings`  (icone engrenage)
- Cliquez sur `Environment Variables`  
- Cliquez sur `Add Environment Variables`  

|   Nom des Variables  |   Description   |   Valeurs à renseigner   |
|---    |---   |---    |
|   DOCKER_USER   |   User Docker Hub   |   Votre nom d'utilisateur sur Docker Hub   |
|   DOCKER_TOKEN   |   Token Docker Hub   |   Un token généré sur Docker Hub dans l'onglet 'Security'   |
|   OC_LETTINGS_DJANGO_SECRET_KEY |  DJANGO SECRET KEY  |   `fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s`   |
| OC_LETTINGS_SENTRY_DNS    | URL Sentry  | l'URL fournie par Sentry lors de la création de l'application dans l'interface Web |
| RENDER_DEPLOY_HOOK  |  Deploy Hook pour Render  |  l'URL du 'deploy hook' fourni par Render lors de la création de l'application dans l'interface Web  |
---

Vous pouvez également consulter le pipeline CircleCI de ce projet [ici](https://app.circleci.com/pipelines/github/TheoSntt/oc-lettings).

## Docker Hub :

[Docker-Hub Théo Sinatti Repository](https://hub.docker.com/r/theosinatti/oc_lettings) stocke les différentes versions de l'image docker de notre application.  

La commande unique pour récupération de l'application en local et son démarrage immédiat est :

`docker run --pull always -p 8080:8080 -e OC_LETTINGS_DJANGO_SECRET_KEY="<Secret Key>" --name oc_lettings_container theosinatti/oc_lettings:latest`

- La DJANGO SECRET KEY doit être renseignée afin que le conteneur s'éxécute
- oc_lettings_container est le nom du container qui sera exécuté 
- theosinatti est le nom du compte Docker Hub  
- latest peux être remplacé par le hash du commit souhaité.

---

## Render :
[L'application sur Render](https://oc-lettings-tx4m.onrender.com)  

Render permet d'heberger notre application.
Pour que l'application fonctionne, il faut définir les mêmes variables que pour le développement en local. Elles doivent être définies au sein de l'interface de Render, dans l'onglet 'Environment'
Pour rappel, ces variables sont : 
- OC_LETTINGS_DJANGO_SECRET_KEY
- OC_LETTINGS_SENTRY_DNS

## Documentation :

La documentation a été réalisée à l'aide de Sphinx et est publiée sur Readthedocs.
Vous pouvez trouver la documentation en ligne de l'application [ici](https://oc-project-13.readthedocs.io/fr/latest/)https://oc-project-13.readthedocs.io/fr/latest/.
