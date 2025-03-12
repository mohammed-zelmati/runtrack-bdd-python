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

        # Requête SQL pour récupérer les noms et les capacités
        query = "SELECT nom, capacite FROM salle"
        cursor.execute(query)

        # Récupérer les résultats
        resultats = cursor.fetchall()

        # # Afficher les résultats en console
        # print("Noms des salles et leurs capacités :")
        # for nom, capacite in resultats:
        #     print(f"Salle : {nom}, Capacité : {capacite}")
        
        # Conversion des résultats en liste
        salles_liste = [(nom, capacite) for nom, capacite in resultats]

        # Afficher les résultats dans une liste
        print("Salles et leurs capacités sous forme de liste :")
        print(salles_liste)

except mysql.connector.Error as err:
    print(f"Erreur : {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")
