import mysql.connector

try:
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="357321zM@.",  
        database="MaNouvelleBase"
    )

    if connection.is_connected():
        print("Connexion réussie à MaNouvelleBase")

        # Création d'un curseur pour exécuter la requête
        cursor = connection.cursor()
        
          # Première requête : employés avec un salaire supérieur à 3 000 €
        print("\nEmployés avec un salaire supérieur à 3 000 € :")
        query1 = "SELECT * FROM employe WHERE salaire > 3000"
        cursor.execute(query1)
        resultats1 = cursor.fetchall()
        for row in resultats1:
            print(row)

        # Deuxième requête : employés et leurs services respectifs
        print("\nEmployés et leurs services respectifs :")
        query2 = """
        SELECT employe.nom AS employe_nom, employe.prenom, employe.salaire, service.nom AS service_nom
        FROM employe
        JOIN service ON employe.id_service = service.id
        """
        cursor.execute(query2)
        resultats2 = cursor.fetchall()
        for employe_nom, prenom, salaire, service_nom in resultats2:
            print(f"Employé : {employe_nom} {prenom}, Salaire : {salaire} €, Service : {service_nom}")
except mysql.connector.Error as err:
    print(f"Erreur : {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connexion fermée")
