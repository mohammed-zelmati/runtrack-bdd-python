import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="357321zM@.",
    database="zoo"
)
cursor = conn.cursor()

def ajouter_animal():
    nom = input("Nom de l'animal : ")
    race = input("Race de l'animal : ")
    id_cage = input("ID de la cage (laisser vide si aucune) : ")
    date_naissance = input("Date de naissance (AAAA-MM-JJ) : ")
    pays_origine = input("Pays d'origine : ")

    query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    values = (nom, race, id_cage if id_cage else None, date_naissance, pays_origine)
    cursor.execute(query, values)
    conn.commit()
    print("Animal ajouté avec succès.")

def ajouter_cage():
    superficie = float(input("Superficie de la cage : "))
    capacite_max = int(input("Capacité maximum de la cage : "))

    query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
    values = (superficie, capacite_max)
    cursor.execute(query, values)
    conn.commit()
    print("Cage ajoutée avec succès.")

def afficher_animaux():
    cursor.execute("SELECT * FROM animal")
    for animal in cursor.fetchall():
        print(animal)

def afficher_animaux_dans_cages():
    query = """
    SELECT c.id AS cage_id, a.nom AS animal_nom
    FROM cage c
    LEFT JOIN animal a ON c.id = a.id_cage
    """
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

def calculer_superficie_totale():
    cursor.execute("SELECT SUM(superficie) FROM cage")
    result = cursor.fetchone()
    print(f"Superficie totale : {result[0]} m²")

def menu():
    while True:
        print("\nMenu :")
        print("1. Ajouter un animal")
        print("2. Ajouter une cage")
        print("3. Afficher tous les animaux")
        print("4. Afficher les animaux dans les cages")
        print("5. Calculer la superficie totale des cages")
        print("6. Quitter")
        choix = input("Votre choix : ")

        if choix == "1":
            ajouter_animal()
        elif choix == "2":
            ajouter_cage()
        elif choix == "3":
            afficher_animaux()
        elif choix == "4":
            afficher_animaux_dans_cages()
        elif choix == "5":
            calculer_superficie_totale()
        elif choix == "6":
            break
        else:
            print("Choix invalide.")

menu()

# Fermeture de la connexion
cursor.close()
conn.close()
