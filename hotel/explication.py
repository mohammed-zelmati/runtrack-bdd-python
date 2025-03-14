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

import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connexion à MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="357321zM@.",  # Remplacez par votre mot de passe
    database="hotel"  # Base de données existante
)
cursor = conn.cursor()

# Fenêtre principale
root = tk.Tk()
root.title("Gestion d'Hôtel")


# *** Gestion des Réservations ***
def afficher_reservations():
    cursor.execute("""
    SELECT reservation.id, client.nom, client.prenom, reservation.date_debut, reservation.date_fin, reservation.tarif_total 
    FROM reservation
    JOIN client ON reservation.id_client = client.id
    """)
    reservations = cursor.fetchall()
    for item in tableau_reservations.get_children():
        tableau_reservations.delete(item)
    for res in reservations:
        tableau_reservations.insert("", "end", values=res)

def ajouter_reservation():
    id_client = entry_id_client.get()
    date_debut = entry_date_debut.get()
    date_fin = entry_date_fin.get()
    tarif_total = entry_tarif_total.get()

    try:
        cursor.execute("""
        INSERT INTO reservation (id_client, date_debut, date_fin, tarif_total) 
        VALUES (%s, %s, %s, %s)
        """, (id_client, date_debut, date_fin, tarif_total))
        conn.commit()
        afficher_reservations()
        messagebox.showinfo("Succès", "Réservation ajoutée avec succès.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de l'ajout : {err}")




def modifier_reservation():
    selected_item = tableau_reservations.selection()
    if not selected_item:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une réservation à modifier.")
        return
    res_id = tableau_reservations.item(selected_item[0], "values")[0]  # ID de la réservation
    nouvelle_date_debut = entry_date_debut.get()
    nouvelle_date_fin = entry_date_fin.get()
    nouveau_tarif_total = entry_tarif_total.get()

    try:
        cursor.execute("""
        UPDATE reservation 
        SET date_debut = %s, date_fin = %s, tarif_total = %s 
        WHERE id = %s
        """, (nouvelle_date_debut, nouvelle_date_fin, nouveau_tarif_total, res_id))
        conn.commit()
        afficher_reservations()
        messagebox.showinfo("Succès", "Réservation modifiée avec succès.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de la modification : {err}")

def supprimer_reservation():
    selected_item = tableau_reservations.selection()
    if not selected_item:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une réservation à supprimer.")
        return
    res_id = tableau_reservations.item(selected_item[0], "values")[0]

    try:
        cursor.execute("DELETE FROM reservation WHERE id = %s", (res_id,))
        conn.commit()
        afficher_reservations()
        messagebox.showinfo("Succès", "Réservation supprimée avec succès.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de la suppression : {err}")

# *** Gestion des Paiements ***
def afficher_paiements():
    cursor.execute("""
    SELECT paiement.id, reservation.id AS reservation_id, paiement.date_paiement, paiement.heure_paiement, paiement.numero_carte, paiement.nom_banque, paiement.code_transaction
    FROM paiement
    JOIN reservation ON paiement.id_reservation = reservation.id
    """)
    paiements = cursor.fetchall()
    for item in tableau_paiements.get_children():
        tableau_paiements.delete(item)
    for pay in paiements:
        tableau_paiements.insert("", "end", values=pay)

def ajouter_paiement():
    id_reservation = entry_id_reservation.get()
    date_paiement = entry_date_paiement.get()
    heure_paiement = entry_heure_paiement.get()
    numero_carte = entry_numero_carte.get()
    nom_banque = entry_nom_banque.get()
    code_transaction = entry_code_transaction.get()

    try:
        cursor.execute("""
        INSERT INTO paiement (id_reservation, date_paiement, heure_paiement, numero_carte, nom_banque, code_transaction)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_reservation, date_paiement, heure_paiement, numero_carte, nom_banque, code_transaction))
        conn.commit()
        afficher_paiements()
        messagebox.showinfo("Succès", "Paiement ajouté avec succès.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de l'ajout : {err}")

# *** Interface graphique Tkinter ***

# Onglets
tabs = ttk.Notebook(root)
tab_reservations = ttk.Frame(tabs)
tab_paiements = ttk.Frame(tabs)
tabs.add(tab_reservations, text="Réservations")
tabs.add(tab_paiements, text="Paiements")
tabs.pack(expand=1, fill="both")

# *** Tab Réservations ***
frame_reservations = ttk.Frame(tab_reservations)
frame_reservations.pack(pady=10)

tableau_reservations = ttk.Treeview(frame_reservations, columns=("id", "nom", "prenom", "date_debut", "date_fin", "tarif_total"), show="headings")
for col in tableau_reservations["columns"]:
    tableau_reservations.heading(col, text=col)
tableau_reservations.pack()

frame_form_reservations = ttk.Frame(tab_reservations)
frame_form_reservations.pack(pady=10)

tk.Label(frame_form_reservations, text="ID Client").grid(row=0, column=0)
entry_id_client = tk.Entry(frame_form_reservations)
entry_id_client.grid(row=0, column=1)

tk.Label(frame_form_reservations, text="Date Début").grid(row=1, column=0)
entry_date_debut = tk.Entry(frame_form_reservations)
entry_date_debut.grid(row=1, column=1)

tk.Label(frame_form_reservations, text="Date Fin").grid(row=2, column=0)
entry_date_fin = tk.Entry(frame_form_reservations)
entry_date_fin.grid(row=2, column=1)

tk.Label(frame_form_reservations, text="Tarif Total").grid(row=3, column=0)
entry_tarif_total = tk.Entry(frame_form_reservations)
entry_tarif_total.grid(row=3, column=1)

tk.Button(frame_form_reservations, text="Ajouter Réservation", command=ajouter_reservation).grid(row=4, column=0)
tk.Button(frame_form_reservations, text="Modifier Réservation", command=modifier_reservation).grid(row=4, column=1)
tk.Button(frame_form_reservations, text="Supprimer Réservation", command=supprimer_reservation).grid(row=4, column=2)
tk.Button(tab_reservations, text="Afficher les Réservations", command=afficher_reservations).pack(pady=10)

# *** Tab Paiements ***
frame_paiements = ttk.Frame(tab_paiements)
frame_paiements.pack(pady=10)

tableau_paiements = ttk.Treeview(frame_paiements, columns=("id", "reservation_id", "date_paiement", "heure_paiement", "numero_carte", "nom_banque", "code_transaction"), show="headings")
for col in tableau_paiements["columns"]:
    tableau_paiements.heading(col, text=col)
tableau_paiements.pack()

frame_form_paiements = ttk.Frame(tab_paiements)
frame_form_paiements.pack(pady=10)

tk.Label(frame_form_paiements, text="ID Réservation").grid(row=0, column=0)
entry_id_reservation = tk.Entry(frame_form_paiements)
entry_id_reservation.grid(row=0, column=1)

tk.Label(frame_form_paiements, text="Date Paiement").grid(row=1, column=0)
entry_date_paiement = tk.Entry(frame_form_paiements)
entry_date_paiement.grid(row=1, column=1)

tk.Label(frame_form_paiements, text="Heure Paiement").grid(row=2, column=0)
entry_heure_paiement = tk.Entry(frame_form_paiements)
entry_heure_paiement.grid(row=2, column=1)

tk.Label(frame_form_paiements, text="Numéro Carte").grid(row=3, column=0)
entry_numero_carte = tk.Entry(frame_form_paiements)
entry_numero_carte.grid(row=3, column=1)

tk.Label(frame_form_paiements, text="Nom Banque").grid(row=4, column=0)
entry_nom_banque = tk.Entry(frame_form_paiements)
entry_nom_banque.grid(row=4, column=1)

tk.Label(frame_form_paiements, text="Code Transaction")

# ----------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Connexion à MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="357321zM@.",  # Remplacez par votre mot de passe
    database="hotel"  # Base de données existante
)
cursor = conn.cursor()

# Fenêtre principale
root = tk.Tk()
root.title("Gestion d'Hôtel")


# *** Gestion des Clients ***
def afficher_clients():
    cursor.execute("SELECT * FROM client")
    clients = cursor.fetchall()
    for item in tableau_clients.get_children():
        tableau_clients.delete(item)
    for client in clients:
        tableau_clients.insert("", "end", values=client)

def ajouter_client():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    date_naissance = entry_date_naissance.get()
    adresse = entry_adresse.get()
    pays_origine = entry_pays.get()
    nationalite = entry_nationalite.get()
    numero_identite = entry_identite.get()
    email = entry_email.get()
    telephone = entry_telephone.get()

    try:
        cursor.execute("""
        INSERT INTO client (nom, prenom, date_naissance, adresse, pays_origine, nationalite, numero_identite, email, telephone)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (nom, prenom, date_naissance, adresse, pays_origine, nationalite, numero_identite, email, telephone))
        conn.commit()
        afficher_clients()
        messagebox.showinfo("Succès", "Client ajouté avec succès.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de l'ajout : {err}")

# *** Gestion des Chambres ***
def afficher_chambres():
    cursor.execute("""
    SELECT chambre.id, chambre.numero_chambre, categorie_chambre.nom, categorie_chambre.prix_par_nuit 
    FROM chambre
    JOIN categorie_chambre ON chambre.id_categorie = categorie_chambre.id
    """)
    chambres = cursor.fetchall()
    for item in tableau_chambres.get_children():
        tableau_chambres.delete(item)
    for chambre in chambres:
        tableau_chambres.insert("", "end", values=chambre)

# *** Onglets ***
tabs = ttk.Notebook(root)
tab_clients = ttk.Frame(tabs)
tab_chambres = ttk.Frame(tabs)
tab_categories = ttk.Frame(tabs)
tab_reservations = ttk.Frame(tabs)
tab_paiements = ttk.Frame(tabs)
tabs.add(tab_clients, text="Clients")
tabs.add(tab_chambres, text="Chambres")
tabs.add(tab_categories, text="Catégories")
tabs.add(tab_reservations, text="Réservations")
tabs.add(tab_paiements, text="Paiements")
tabs.pack(expand=1, fill="both")

# *** Tab Clients ***
frame_clients = ttk.Frame(tab_clients)
frame_clients.pack(pady=10)

tableau_clients = ttk.Treeview(frame_clients, columns=("id", "nom", "prenom", "date_naissance", "adresse", "pays_origine", "nationalite", "numero_identite", "email", "telephone"), show="headings")
for col in tableau_clients["columns"]:
    tableau_clients.heading(col, text=col)
tableau_clients.pack()

frame_form_clients = ttk.Frame(tab_clients)
frame_form_clients.pack(pady=10)

tk.Label(frame_form_clients, text="Nom").grid(row=0, column=0)
entry_nom = tk.Entry(frame_form_clients)
entry_nom.grid(row=0, column=1)

tk.Label(frame_form_clients, text="Prénom").grid(row=1, column=0)
entry_prenom = tk.Entry(frame_form_clients)
entry_prenom.grid(row=1, column=1)

tk.Label(frame_form_clients, text="Date de Naissance").grid(row=2, column=0)
entry_date_naissance = tk.Entry(frame_form_clients)
entry_date_naissance.grid(row=2, column=1)

tk.Label(frame_form_clients, text="Adresse").grid(row=3, column=0)
entry_adresse = tk.Entry(frame_form_clients)
entry_adresse.grid(row=3, column=1)

tk.Label(frame_form_clients, text="Pays d'origine").grid(row=4, column=0)
entry_pays = tk.Entry(frame_form_clients)
entry_pays.grid(row=4, column=1)

tk.Label(frame_form_clients, text="Nationalité").grid(row=5, column=0)
entry_nationalite = tk.Entry(frame_form_clients)
entry_nationalite.grid(row=5, column=1)

tk.Label(frame_form_clients, text="Numéro d'identité").grid(row=6, column=0)
entry_identite = tk.Entry(frame_form_clients)
entry_identite.grid(row=6, column=1)

tk.Label(frame_form_clients, text="Email").grid(row=7, column=0)
entry_email = tk.Entry(frame_form_clients)
entry_email.grid(row=7, column=1)

tk.Label(frame_form_clients, text="Téléphone").grid(row=8, column=0)
entry_telephone = tk.Entry(frame_form_clients)
entry_telephone.grid(row=8, column=1)

tk.Button(frame_form_clients, text="Ajouter Client", command=ajouter_client).grid(row=9, column=0, columnspan=2)
tk.Button(tab_clients, text="Afficher les Clients", command=afficher_clients).pack(pady=10)

# *** Tab Chambres ***
frame_chambres = ttk.Frame(tab_chambres)
frame_chambres.pack(pady=10)

tableau_chambres = ttk.Treeview(frame_chambres, columns=("id", "numero_chambre", "categorie", "prix_par_nuit"), show="headings")
for col in tableau_chambres["columns"]:
    tableau_chambres.heading(col, text=col)
tableau_chambres.pack()

tk.Button(tab_chambres, text="Afficher les Chambres", command=afficher_chambres).pack(pady=10)

# *** Charger les données au démarrage ***
afficher_clients()
afficher_chambres()

# Lancer l'application
root.mainloop()