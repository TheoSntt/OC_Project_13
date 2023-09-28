Installation
============

Prérequis pour exécuter l'application en local :
- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
- Compte Sentry

.. note::

    Si vous utilisez Windows et PowerShell, les commandes seront les
    mêmes que celles présentées ci-dessous sauf :

        - pour activer l'environnement virtuel : ``.\venv\Scripts\Activate.ps1``
        - remplacer ``which <my-command>`` par ``(Get-Command <my-command>).Path``

Cloner le repository GitHub
---------------------------

Exécutez les commandes suivantes :

    - ``cd /path/to/put/project/in``
    - ``git clone https://github.com/TheoSntt/OC_Project_13.git``

Créer l'environnement virtuel et installer les dépendances
----------------------------------------------------------

Exécutez les commandes suivantes :

    - ``cd /path/to/Python-OC-Lettings-FR``
    - ``python -m venv venv``
    - ``apt-get install python3-venv`` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
    - Activer l'environnement ``source venv/bin/activate``
    - ``pip install --requirement requirements.txt``
    - Créer un fichier ``.env`` pour y indiquer :

    .. code-block:: console

        SECRET_KEY=<la SECRET_KEY de votre projet Django>

Lier le projet à Sentry
-----------------------

Sentry est une plateforme qui signale automatiquement les erreurs et les
exceptions du projet. Il permet également la surveillance des performances.

Exécutez les commandes suivantes :

    - Créer un compte Sentry_
    - Créer un projet avec la plateforme ``Django``
    - Récupérer la clé dsn et l'intégrer dans votre fichier ``.env``

    .. code-block:: console

        SENTRY_DSN=<la clé dsn de votre projet Sentry>

    - Se connecter sur votre compte Sentry pour visualiser les logs récupérés par Sentry

.. _Sentry: <https://sentry.io/signup/?original_referrer=https%3A%2F%2Fdocs.sentry.io%2F>
