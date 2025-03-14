# 1. À partir du scénario suivant, modélisez et créez la base de données SQL :
# Un client peut effectuer une ou plusieurs réservations, Les coordonnées 
# du client enregistrés lors de la réservation sont le Nom, Prénom,
# Date de Naissance, Adresse, Pays d'origine, Nationalité, N d’identité 
# ou N de passeport, Email et N de Téléphone, Une réservation peut concerner 
# une ou plusieurs chambres de l’hotel (un client peut choisir plusieurs 
# chambres dans une réservation).
# Dans une réservation, une chambre est réservée selon une durée, date de début,
# date de fin et Tarif total a payer, Chaque chambre appartient 
# a une et une seule catégorie de chambres, Chaque catégorie est 
# caractérisée par son nom, sa description et le prix par nuitée 
# des chambres lui appartenant. Après la réservation, le client 
# procède a un paiement qui correspond a une et une seule réservation. 
# Pour chaque paiement, on enregistre sa date, son heure, le N de carte 
# de débit et le nom de banque du client ainsi qu’un code de transaction
# L'objectif est d'écrire le script SQL permettant de créer ces tables avec les bonnes relations.

# 2. Insertion de Données
# Ajoutez au moins 10 clients, 5 catégories de chambres, 15 réservations et 15 paiements.
# Vérifiez l’intégrité des données (ex : une réservation doit être liée à un client).

# 3. SQL Challenge
# Répondez aux requêtes suivantes le plus vite possible :
# Lister tous les clients ayant réservé plusieurs chambres.
# Calculer le chiffre d’affaires total de l’hôtel sur un mois donné.
# Trouver la catégorie de chambre la plus réservée.
# L’équipe la plus rapide et précise remporte le challenge.
# ------------------------------------------------------
