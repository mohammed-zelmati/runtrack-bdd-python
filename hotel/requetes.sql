-- Création de la base de données
CREATE DATABASE hotel;
USE hotel;

-- Table client
CREATE TABLE client (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    adresse VARCHAR(255),
    pays_origine VARCHAR(100),
    nationalite VARCHAR(100),
    numero_identite VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    telephone VARCHAR(20)
);

-- Table catégorie de chambres
CREATE TABLE categorie_chambre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    description TEXT,
    prix_par_nuit DECIMAL(10, 2) NOT NULL
);

-- Table chambre
CREATE TABLE chambre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_chambre INT UNIQUE NOT NULL,
    id_categorie INT NOT NULL,
    FOREIGN KEY (id_categorie) REFERENCES categorie_chambre(id)
);

-- Table réservation
CREATE TABLE reservation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_client INT NOT NULL,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    tarif_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_client) REFERENCES client(id)
);

-- Table de liaison entre réservation et chambre (relation "une réservation concerne plusieurs chambres")
CREATE TABLE reservation_chambre (
    id_reservation INT NOT NULL,
    id_chambre INT NOT NULL,
    PRIMARY KEY (id_reservation, id_chambre),
    FOREIGN KEY (id_reservation) REFERENCES reservation(id),
    FOREIGN KEY (id_chambre) REFERENCES chambre(id)
);

-- Table paiement
CREATE TABLE paiement (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_reservation INT NOT NULL,
    date_paiement DATE NOT NULL,
    heure_paiement TIME NOT NULL,
    numero_carte VARCHAR(20) NOT NULL,
    nom_banque VARCHAR(100),
    code_transaction VARCHAR(50) UNIQUE NOT NULL,
    FOREIGN KEY (id_reservation) REFERENCES reservation(id)
);

-- Lister les clients ayant réservé plusieurs chambres
SELECT c.nom, c.prenom, COUNT(rc.id_chambre) AS nombre_chambres
FROM client c
JOIN reservation r ON c.id = r.id_client
JOIN reservation_chambre rc ON r.id = rc.id_reservation
GROUP BY c.id
HAVING COUNT(rc.id_chambre) > 1;

-- Calculer le chiffre d’affaires total sur un mois donné
-- Exemple pour mars 2025 :
SELECT SUM(tarif_total) AS chiffre_affaires_total
FROM reservation
WHERE MONTH(date_debut) = 3 AND YEAR(date_debut) = 2025;

-- Trouver la catégorie de chambre la plus réservée
SELECT cc.nom, COUNT(rc.id_chambre) AS nombre_reservations
FROM categorie_chambre cc
JOIN chambre ch ON cc.id = ch.id_categorie
JOIN reservation_chambre rc ON ch.id = rc.id_chambre
GROUP BY cc.id
ORDER BY nombre_reservations DESC
LIMIT 1;
