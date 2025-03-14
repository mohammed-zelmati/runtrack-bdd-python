import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="357321zM@.", 
)
cursor = conn.cursor()

# Création des tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS client (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telephone VARCHAR(20)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS chambre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_chambre INT UNIQUE NOT NULL,
    type VARCHAR(50) NOT NULL,
    prix_par_nuit DECIMAL(10, 2) NOT NULL,
    statut VARCHAR(50) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    chambre_id INT NOT NULL,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    FOREIGN KEY(client_id) REFERENCES client(id),
    FOREIGN KEY(chambre_id) REFERENCES chambre(id)
)
""")

conn.commit()

# Ajouter un client
def ajouter_client(nom, email, telephone):
    cursor.execute("""
    INSERT INTO client (nom, email, telephone)
    VALUES (%s, %s, %s)
    """, (nom, email, telephone))
    conn.commit()
    print("Client ajouté avec succès.")

# Ajouter une chambre
def ajouter_chambre(numero_chambre, type, prix_par_nuit, statut):
    cursor.execute("""
    INSERT INTO chambre (numero_chambre, type, prix_par_nuit, statut)
    VALUES (%s, %s, %s, %s)
    """, (numero_chambre, type, prix_par_nuit, statut))
    conn.commit()
    print("Chambre ajoutée avec succès.")

# Effectuer une réservation
def effectuer_reservation(client_id, chambre_id, date_debut, date_fin):
    cursor.execute("""
    INSERT INTO reservation (client_id, chambre_id, date_debut, date_fin)
    VALUES (%s, %s, %s, %s)
    """, (client_id, chambre_id, date_debut, date_fin))
    conn.commit()
    print("Réservation effectuée avec succès.")

# Modifier une réservation
def modifier_reservation(reservation_id, nouvelle_date_debut, nouvelle_date_fin):
    cursor.execute("""
    UPDATE reservation
    SET date_debut = %s, date_fin = %s
    WHERE id = %s
    """, (nouvelle_date_debut, nouvelle_date_fin, reservation_id))
    conn.commit()
    print("Réservation modifiée avec succès.")

# Supprimer une réservation
def supprimer_reservation(reservation_id):
    cursor.execute("""
    DELETE FROM reservation
    WHERE id = %s
    """, (reservation_id,))
    conn.commit()
    print("Réservation supprimée avec succès.")

# Exemple d'utilisation
ajouter_client("Mounir", "mounir@example.com", "123456789")
ajouter_chambre(101, "Double", 120.5, "Disponible")
effectuer_reservation(1, 1, "2025-03-15", "2025-03-20")
modifier_reservation(1, "2025-03-16", "2025-03-21")
supprimer_reservation(1)

# Fermer la connexion
conn.close()
