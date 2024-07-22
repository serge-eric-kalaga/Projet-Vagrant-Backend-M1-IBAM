# Projet-Vagrant-M1-IBAM
Projet de Master 1 (IBAM) portant sur Vagrant

Ce projet est une application de gestion de tâches qui permet de créer, lire, mettre à jour et supprimer des tâches. Les tâches sont associées à des utilisateurs et contiennent des informations telles que le nom de la tâche, sa description, son statut d'achèvement, la date de création, et l'utilisateur responsable.

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
    },
    {
        "id": 2,
        "name": "Task 2",
        "description": "Description of task 2",
        "is_completed": true,
        "date_creation": "2024-07-15T09:21:45Z",
    }
]
```


### Modèle JSON pour envoyer une tâche (POST)

```json

  {
      "id": 1,
      "name": "Task 1",
      "description": "Description of task 1",
      "is_completed": false,
      "date_creation": "2024-07-16T12:34:56Z",
  }
```

