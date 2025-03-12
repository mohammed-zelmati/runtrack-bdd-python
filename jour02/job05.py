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

        
        # Requête SQL pour calculer la superficie totale
        query = "SELECT SUM(superficie) AS total_superficie FROM etage"
        cursor.execute(query)

        # Récupérer le résultat de la requête
        result = cursor.fetchone()
        total_superficie = result[0]  # La première valeur du résultat

        # Afficher le message avec la superficie totale
        print(f"La superficie de La Plateforme est de {total_superficie} m2")

except mysql.connector.Error as err:
    print(f"Erreur : {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")
