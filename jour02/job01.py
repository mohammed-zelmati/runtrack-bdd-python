import mysql.connector

# Connexion à la base de données
try:
    connection = mysql.connector.connect(
        host="localhost", # L'adresse de votre serveur
        user="root", # nom d'utilisateur
        password="357321zM@.", 
        database="LaPlateforme"  # Nom de votre base de données
    )
    
    if connection.is_connected():
        print("Connexion réussie à LaPlateforme")

        # Création d'un curseur pour exécuter les requêtes
        cursor = connection.cursor()

        # Requête SQL pour récupérer tous les étudiants
        query = "SELECT * FROM etudiant"
        cursor.execute(query)

        # Récupérer et afficher les résultats
        resultats = cursor.fetchall()
        for row in resultats:
            print(row)  # Chaque ligne correspond à un étudiant 
except mysql.connector.Error as err:
    print(f"Erreur de connexion : {err}")

finally:
    if connection.is_connected():
        connection.close()
        print("Connexion fermée")
