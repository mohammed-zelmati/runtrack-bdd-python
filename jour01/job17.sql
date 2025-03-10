-- Pour corriger l'age de "Spaghetti Betty" à 20 ans au lieu de 23 ans dans la table etudiant
UPDATE etudiant
SET age = 20
WHERE nom = 'Spaghetti' AND prenom = 'Betty';

-- Pour confirmer la mise à jour de l'âge 
SELECT * FROM etudiant WHERE nom ='Spaghetti' AND prenom = 'Betty';
