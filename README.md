# Projet-Vagrant-M1-IBAM

Projet de Master 1 (IBAM) portant sur Vagrant

Ce projet est une application de gestion de tâches qui permet de créer, lire, mettre à jour et supprimer des tâches. Les tâches sont associées à des utilisateurs et contiennent des informations telles que le nom de la tâche, sa description, son statut d'achèvement, la date de création, et l'utilisateur responsable.

## Comment cloner le projet

Pour cloner le projet et ses sous-modules, utilisez les commandes suivantes :

```
git clone https://github.com/serge-eric-kalaga/Projet-Vagrant-Backend-M1-IBAM.git
git submodule update --init --recursive
```

## Comment lancer le projet

Pour lancer le projet, vous devez avoir Docker et Docker Compose installés sur votre machine. Ensuite, suivez ces étapes :

1. Assurez-vous d'être dans le répertoire racine du projet.
2. Exécutez la commande suivante :

```
docker compose up --build
```

## URLs du projet

- API Backend : `http://localhost:8080`
- Frontend : `http://localhost:4200`

## Structure JSON

### Modèle JSON pour obtenir la liste des tâches (GET)

```json
[
    {
        "id": 1,
        "name": "Task 1",
        "description": "Description of task 1",
        "is_completed": false,
        "date_creation": "2024-07-16T12:34:56Z",
        "date_modification": "2024-07-16T12:34:56Z"
    },
    {
        "id": 2,
        "name": "Task 2",
        "description": "Description of task 2",
        "is_completed": true,
        "date_creation": "2024-07-15T09:21:45Z",
        "date_modification": "2024-07-16T12:34:56Z"
    }
]
```

### Modèle JSON pour envoyer ou modifierune tâche (POST)

```json
{
    "id": 1,
    "name": "Task 1",
    "description": "Description of task 1",
    "is_completed": false,
    "date_creation": "2024-07-16T12:34:56Z"
}
```