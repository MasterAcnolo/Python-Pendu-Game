import random

def choisir_mot():
    mots = ["Mot", "ordinateur", "programmation", "developpeur", "algorithmique", "GitHub"]
    return random.choice(mots)

def jouer_pendu(mot):
    taille_mot = len(mot)
    lettres_trouvees = ['_'] * taille_mot
    lettres_utilisees = []
    erreurs_max = 6
    erreurs = 0
    
    print("Bienvenue au jeu du Pendu !")
    print("Le mot à deviner contient", taille_mot, "lettres.")
    print_affichage_mot(lettres_trouvees)
    
    while '_' in lettres_trouvees and erreurs < erreurs_max:
        lettre = demander_lettre(lettres_utilisees)
        
        if lettre in mot:
            for i in range(taille_mot):
                if mot[i] == lettre:
                    lettres_trouvees[i] = lettre
            print("Bonne devinette !")
        else:
            erreurs += 1
            print("Désolé, cette lettre ne fait pas partie du mot.")
            print("Il vous reste", erreurs_max - erreurs, "tentatives.")
            
        lettres_utilisees.append(lettre)
        print_affichage_mot(lettres_trouvees)
        
    if '_' not in lettres_trouvees:
        print("Félicitations ! Vous avez deviné le mot :", mot)
    else:
        print("Désolé, vous avez atteint le nombre maximum d'erreurs. Le mot était :", mot)

def demander_lettre(lettres_utilisees):
    lettre = input("Devinez une lettre : ").lower()
    while len(lettre) != 1 or not lettre.isalpha() or lettre in lettres_utilisees:
        print("Veuillez entrer une seule lettre qui n'a pas déjà été utilisée.")
        lettre = input("Devinez une lettre : ").lower()
    return lettre

def print_affichage_mot(lettres_trouvees):
    print("Mot actuel :", " ".join(lettres_trouvees))

mot_a_deviner = choisir_mot()
jouer_pendu(mot_a_deviner)
