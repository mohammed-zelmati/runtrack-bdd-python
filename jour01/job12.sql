-- Pour ajouter Martin Dupuis à la table etudiant
INSERT INTO etudiant (nom, prenom, age, email) 
VALUES ('Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io');

-- Pour récupérer tous les membres d'une même famille
SELECT * FROM etudiant WHERE nom = 'Dupuis';
