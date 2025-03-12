import mysql.connector

try:
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host="localhost", # Adresse du serveur
        user="root",  # nom d'utilisateur MySQL
        password="357321zM@.",
        database="LaPlateforme"    # Nom de base de données
    )

    if connection.is_connected():
        print("Connexion réussie à LaPlateforme")

        # Création d'un curseur pour exécuter la requête
        cursor = connection.cursor()

        
        # Requête SQL pour calculer la capacité totale
        query = "SELECT SUM(capacite) AS capacite_totale FROM salle"
        cursor.execute(query)

        # Récupérer le résultat de la requête
        result = cursor.fetchone()
        capacite_totale = result[0]  # La première valeur du résultat

        # Afficher le résultat
        print(f"La capacité totale des salles est de {capacite_totale}")

except mysql.connector.Error as err:
    print(f"Erreur : {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")
