def ajouter_tache(taches, titre):
    titre_propre = titre.strip()
    if titre_propre == "":
        return taches
    nouvel_id = len(taches) + 1

    nouvelle_tache = {
        "id": nouvel_id,
        "titre": titre_propre,
        "fait": False
    }
    taches.append(nouvelle_tache)
    return taches






