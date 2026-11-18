while True :
    print("1. Ajouter une tâche")
    print ("2. Voir mes tâche")
    print ("3. Quitter")

    choix = input("entrer votre choix : " ).strip()
    if choix == "1" :
        print("Ajout bientot")
    elif choix == "2" :
        print("Liste bientot")
    elif choix == "3":
        print("Aurevoir")
        break
    else:
        print("Choix inconnu")
        