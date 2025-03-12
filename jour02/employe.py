import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
            print("Connexion réussie à la base de données")
        except mysql.connector.Error as err:
            print(f"Erreur de connexion : {err}")

    def creer_employe(self, nom, prenom, salaire, id_service):
        """Insère un nouvel employé dans la table."""
        try:
            query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query, (nom, prenom, salaire, id_service))
            self.connection.commit()
            print("Employé ajouté avec succès")
        except mysql.connector.Error as err:
            print(f"Erreur lors de l'insertion : {err}")

    def lire_employes(self):
        """Récupère et affiche tous les employés."""
        try:
            query = "SELECT * FROM employe"
            self.cursor.execute(query)
            employes = self.cursor.fetchall()
            print("Liste des employés :")
            for employe in employes:
                print(employe)
        except mysql.connector.Error as err:
            print(f"Erreur lors de la récupération : {err}")

    def mettre_a_jour_employe(self, id_employe, nom=None, prenom=None, salaire=None, id_service=None):
        """Met à jour les informations d'un employé spécifique."""
        try:
            updates = []
            values = []
            if nom:
                updates.append("nom = %s")
                values.append(nom)
            if prenom:
                updates.append("prenom = %s")
                values.append(prenom)
            if salaire:
                updates.append("salaire = %s")
                values.append(salaire)
            if id_service:
                updates.append("id_service = %s")
                values.append(id_service)
            values.append(id_employe)

            query = f"UPDATE employe SET {', '.join(updates)} WHERE id = %s"
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Employé mis à jour avec succès")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la mise à jour : {err}")

    def supprimer_employe(self, id_employe):
        """Supprime un employé de la table."""
        try:
            query = "DELETE FROM employe WHERE id = %s"
            self.cursor.execute(query, (id_employe,))
            self.connection.commit()
            print("Employé supprimé avec succès")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la suppression : {err}")

    def fermer_connexion(self):
        """Ferme la connexion à la base de données."""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Connexion fermée")


# Exemple d'utilisation
if __name__ == "__main__":
    employe_db = Employe(host="localhost", user="root", password="357321zM@.", database="MaNouvelleBase")

    # Ajouter un nouvel employé
    employe_db.creer_employe("Dupont", "Jean", 3500.50, 1)

    # Lire les employés
    employe_db.lire_employes()

    # Mettre à jour un employé
    employe_db.mettre_a_jour_employe(1, nom="Dupont", prenom="Jean-Claude", salaire=4000.00)

    # Lire les employés après mise à jour
    employe_db.lire_employes()

    # Supprimer un employé
    employe_db.supprimer_employe(1)

    # Lire les employés après suppression
    employe_db.lire_employes()

    # Fermer la connexion
    employe_db.fermer_connexion()
