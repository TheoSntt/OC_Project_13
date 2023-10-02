.. OC-lettings documentation master file, created by
   sphinx-quickstart on Thu Aug 10 11:08:55 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenue dans la documentation du site Web d'Orange County lettings !
======================================================================

Orange County Lettings est une plateforme de location de biens immobiliers.
Le site Web d'OC Lettings permet de consulter les différentes locations disponibles
ainsi que les profils des utilisateurs inscrits sur la plateforme.

Technologies et langages de programmation
-----------------------------------------

Cette application est programmée avec Python et Django.

Les données sont stockées dans la base de données SQLite3.

Les différentes plateformes utilisées sont :

   - GitHub, pour sauvegarder le code et chacune de ses versions,
   - Sentry, pour le logging des erreurs (et autres événements) du site,
   - Docker, pour la conteneurisation,
   - CircleCI, pour la mise en place de l'intégration et la livraison continues du code,
   - Render, pour le déploiement de l'application.

.. toctree::
   :maxdepth: 2
   :caption: Navigation:

   manual
   install
   bdd
   dev
