# Création d'une application pour un système de sondage avec MongoDB

## Identité du projet
**Auteur:**  Sarah Barrabé  
**Framework:**  Django  
**Github:**  https://github.com/Sarouman54/FormNosql  
**Nom du site web:**  CreaSurvey  

## Instructions
Une fois le projet cloné, il vous suffira de vous déplacer dans le dossier `src` et de lancer la commande `python manage.py migrate`.
Cette commande aura pour but de créer la base de données MongoDB à l'adresse 127.0.0.1:27017 avec les tables associées au système d'authentification.  

Ensuite au choix vous pouvez soit lancer la commande `python manage.py runserver` afin de démarrer le serveur à l'adresse 127.0.0.1:8000 soit lancer la commande facultative `python manage.py createsuperuser` afin de créer un super utilisateur dont le système de connexion se trouvera à l'adresse 127.0.0.1:8000/admin. La non création d'un super utilisateur ne changera en rien le fonctionnement de l'application, celui-ci permet simplement de voir les divers utilisateurs qui existent.  

## Routes disponibles
`/` -> page d'accueil avec la liste de tous les sondages
`/newsurvey` -> page de création d'un nouveau sondage
`/listsurvey` -> page regroupant la liste des sondages de l'utilisateur connecté
`/listsurvey/update/<survey_name>` -> page de modification d'un sondage
`/listsurvey/delete/<survey_name>` -> page de suppression d'un sondage
`/survey/<survey_name>` -> page de réponse à un sondage
`/signin` -> page de connexion
`/signout` -> page de déconnexion
`/signup` -> page d'inscription
