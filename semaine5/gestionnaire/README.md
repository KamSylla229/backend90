# Gestionnaire de tâches en ligne de commande

Un petit programme Python pour ajouter et consulter ses tâches depuis le terminal. Les tâches sont sauvegardées dans un fichier JSON et restent disponibles après la fermeture du programme.

Projet réalisé pendant la semaine 5 du challenge #Backend90.

## Fonctionnalités

- Ajouter une tâche (un titre vide ou fait seulement d'espaces est refusé)
- Voir la liste de ses tâches
- Sauvegarde automatique dans `taches.json`
- Aucun plantage en cas de mauvais choix dans le menu
- 10 tests automatiques avec pytest

## Prérequis

- Python 3.11 ou plus récent
- Git
- Sous Windows : utiliser Git Bash

## Installation

```bash
git clone https://github.com/KamSylla229/backend90.git
cd backend90/semaine5/gestionnaire
python -m venv .venv
source .venv/Scripts/activate      # Windows (Git Bash)
# source .venv/bin/activate        # Linux / macOS
pip install -r requirements.txt
```

Le mot `(.venv)` doit apparaître dans le terminal : cela veut dire que l'environnement virtuel est activé.

### Problème possible : erreur SSL pendant `pip install`

Si vous voyez `CERTIFICATE_VERIFY_FAILED`, un antivirus ou le réseau inspecte peut-être les connexions HTTPS. Relancez avec :

```bash
pip install --use-feature=truststore -r requirements.txt
```

## Utilisation

```bash
python main.py
```

Exemple :

```
1. Ajouter une tâche
2. Voir mes tâches
3. Quitter
entrer votre choix : 1
entrer la nouvelle tâche : Préparer le README
Tâche ajoutée
entrer votre choix : 2
1 - Préparer le README
entrer votre choix : 3
Au revoir
```

## Tests

```bash
pytest
```

Résultat attendu : `10 passed`.

## Structure du projet

| Fichier | Rôle |
|---|---|
| `main.py` | Le chef : affiche le menu et appelle les autres fichiers |
| `taches.py` | Les règles : `ajouter_tache` (titre nettoyé, titre vide refusé, id automatique) |
| `stockage.py` | Le cahier : `sauvegarder_taches` et `charger_taches` (JSON) |
| `test_taches.py` | 6 tests de l'ajout de tâches |
| `test_stockage.py` | 4 tests de la sauvegarde et du chargement |
| `requirements.txt` | Les outils à installer (pytest et ses dépendances) |
| `taches.json` | Créé automatiquement au premier ajout, non versionné |

## Auteur

Kamel Sylla — challenge #Backend90 (GitHub : KamSylla229)