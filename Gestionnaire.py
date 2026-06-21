etudiants = [
    {"nom": "Ali", "note": 15},
    {"nom": "Sara", "note": 12},
    {"nom": "Yanis", "note": 18},
    {"nom": "Lina", "note": 16},
    {"nom": "Emma", "note": 14}
]

while True:
    print("==Gestionnaire de Classe==")
    print("1. Afficher les élèves")
    print("2. Afficher les notes obtenues par les élèves")
    print("3. Afficher la moyenne des notes obtenues.")
    print("4. Afficher le(a) meilleur(e) élève")
    print("5. Modifier la note d'un élève")
    print("6. Ajouter un élève")
    print("7. Supprimmer un élève")
    print("8. Quitter")

    choix = int(input("Choisir un numéro: "))


    if choix == 1:
        for e in etudiants:
            print(e["nom"])

    elif choix == 2:
        for e in etudiants:
            print(e["note"], e["nom"])

    elif choix == 3:
        somme = 0
        count = 0
        for e in etudiants:
            somme += e["note"]
            count +=1
        moyenne = somme / count
        print(moyenne)

    elif choix == 4:
        meilleur = etudiants[0]
        for e in etudiants:
            if e["note"] > meilleur["note"]:
                meilleur = e
        print(meilleur["nom"], meilleur["note"])

    elif choix == 5:
        nom = input("Nom: ")
        note = int(input("Note: "))
        for e in etudiants:
            if e["nom"] == nom:
                e["note"] = note
        print("Note changée !")

    elif choix == 6:
        nom = input("Nom: ")
        note = float(input("Note: "))
        etudiants.append({"nom": nom, "note": note})
        print("Élève ajouté(e)")

    elif choix == 7:
        nom = input("Élève à supprimer: ")
        for e in etudiants:
            if e["nom"] == nom:
                etudiants.remove(e)

    elif choix == 8:
        print("Au revoir !")
        break
