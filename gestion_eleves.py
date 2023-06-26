def ajouter_eleve():
    id_eleve = input("Entrez l'identifiant de l'élève : ")
    nom_eleve = input("Entrez le nom de l'élève : ")
    eleves[id_eleve] = nom_eleve
    print("Élève ajouté avec succès !")

def modifier_eleve():
    id_eleve = input("Entrez l'identifiant de l'élève à modifier : ")
    if id_eleve in eleves:
        nouveau_nom = input("Entrez le nouveau nom de l'élève : ")
        eleves[id_eleve] = nouveau_nom
        print("Élève mis à jour avec succès !")
    else:
        print("L'élève n'existe pas.")
