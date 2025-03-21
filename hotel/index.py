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

def ajouter_reservation():
    id_client = entry_id_client.get()
    date_debut = entry_date_debut.get()
    date_fin = entry_date_fin.get()
    tarif_total = entry_tarif_total.get()

    try:
        # Vérifier si le client existe
        cursor.execute("SELECT * FROM client WHERE id = %s", (id_client,))
        client = cursor.fetchone()

        if not client:
            # Si le client n'existe pas, ajouter le client
            ajouter_client_popup = tk.Toplevel(root)
            ajouter_client_popup.title("Ajouter un client")

            # Champs pour ajouter un nouveau client
            tk.Label(ajouter_client_popup, text="Nom").grid(row=0, column=0)
            popup_nom = tk.Entry(ajouter_client_popup)
            popup_nom.grid(row=0, column=1)

            tk.Label(ajouter_client_popup, text="Prénom").grid(row=1, column=0)
            popup_prenom = tk.Entry(ajouter_client_popup)
            popup_prenom.grid(row=1, column=1)

            tk.Label(ajouter_client_popup, text="Date de Naissance").grid(row=2, column=0)
            popup_date_naissance = tk.Entry(ajouter_client_popup)
            popup_date_naissance.grid(row=2, column=1)

            tk.Label(ajouter_client_popup, text="Adresse").grid(row=3, column=0)
            popup_adresse = tk.Entry(ajouter_client_popup)
            popup_adresse.grid(row=3, column=1)

            tk.Label(ajouter_client_popup, text="Pays d'origine").grid(row=4, column=0)
            popup_pays = tk.Entry(ajouter_client_popup)
            popup_pays.grid(row=4, column=1)

            tk.Label(ajouter_client_popup, text="Nationalité").grid(row=5, column=0)
            popup_nationalite = tk.Entry(ajouter_client_popup)
            popup_nationalite.grid(row=5, column=1)

            tk.Label(ajouter_client_popup, text="Numéro d'identité").grid(row=6, column=0)
            popup_identite = tk.Entry(ajouter_client_popup)
            popup_identite.grid(row=6, column=1)

            tk.Label(ajouter_client_popup, text="Email").grid(row=7, column=0)
            popup_email = tk.Entry(ajouter_client_popup)
            popup_email.grid(row=7, column=1)

            tk.Label(ajouter_client_popup, text="Téléphone").grid(row=8, column=0)
            popup_telephone = tk.Entry(ajouter_client_popup)
            popup_telephone.grid(row=8, column=1)

            # Fonction pour sauvegarder le client
            def sauvegarder_client():
                try:
                    cursor.execute("""
                    INSERT INTO client (nom, prenom, date_naissance, adresse, pays_origine, nationalite, numero_identite, email, telephone)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                        popup_nom.get(),
                        popup_prenom.get(),
                        popup_date_naissance.get(),
                        popup_adresse.get(),
                        popup_pays.get(),
                        popup_nationalite.get(),
                        popup_identite.get(),
                        popup_email.get(),
                        popup_telephone.get()
                    ))
                    conn.commit()
                    ajouter_client_popup.destroy()
                    messagebox.showinfo("Succès", "Client ajouté avec succès.")
                except mysql.connector.Error as err:
                    messagebox.showerror("Erreur", f"Erreur lors de l'ajout du client : {err}")

            tk.Button(ajouter_client_popup, text="Enregistrer le client", command=sauvegarder_client).grid(row=9, column=0, columnspan=2)
            return  # Attendre que le client soit ajouté avant d'ajouter la réservation

        # Si le client existe ou vient d'être ajouté, ajouter la réservation
        cursor.execute("""
        INSERT INTO reservation (id_client, date_debut, date_fin, tarif_total) 
        VALUES (%s, %s, %s, %s)
        """, (id_client, date_debut, date_fin, tarif_total))
        conn.commit()
        afficher_reservations()
        messagebox.showinfo("Succès", "Réservation ajoutée avec succès.")
    except mysql.connector.Error as err:
        messagebox.showerror("Erreur", f"Erreur lors de l'ajout de la réservation : {err}")


# Afficher les clients existants
def afficher_clients():
    cursor.execute("SELECT * FROM client")
    clients = cursor.fetchall()
    for item in tableau_clients.get_children():
        tableau_clients.delete(item)
    for client in clients:
        tableau_clients.insert("", "end", values=client)




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
# tab_clients = ttk.Frame(tabs)
tabs.add(tab_reservations, text="Réservations")
tabs.add(tab_paiements, text="Paiements")
# tabs.add(tab_clients, text="Clients")
tabs.pack(expand=1, fill="both")

# *** Tab Réservations ***
frame_reservations = ttk.Frame(tab_reservations)
frame_reservations.pack(pady=7)


# *** Ajout d'un tableau des clients dans l'onglet Réservations ***
frame_clients_reservations = ttk.Frame(tab_reservations)
frame_clients_reservations.pack(pady=7)

tk.Label(frame_clients_reservations, text="Liste des clients existants").pack()
tableau_clients = ttk.Treeview(frame_clients_reservations, columns=("id", "nom", "prenom", "date_naissance", "adresse", "pays_origine", "nationalite", "numero_identite", "email", "telephone"), show="headings")
for col in tableau_clients["columns"]:
    tableau_clients.heading(col, text=col)
tableau_clients.pack()

# Bouton pour afficher les clients après l'ajout d'un client ou plusieurs clients
tk.Button(frame_clients_reservations, text="Afficher les Clients", command=afficher_clients).pack(pady=10)



tableau_reservations = ttk.Treeview(frame_reservations, columns=("id", "nom", "prenom", "date_debut", "date_fin", "tarif_total"), show="headings")
for col in tableau_reservations["columns"]:
    tableau_reservations.heading(col, text=col)
tableau_reservations.pack()

frame_form_reservations = ttk.Frame(tab_reservations)
frame_form_reservations.pack(pady=7)

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
frame_paiements.pack(pady=7)

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

tk.Label(frame_form_paiements, text="Code Transaction").grid(row=5, column=0)
entry_code_transaction = tk.Entry(frame_form_paiements)
entry_code_transaction.grid(row=5, column=1)

tk.Button(frame_form_paiements, text="Ajouter Paiement", command=ajouter_paiement).grid(row=6, column=0, columnspan=2)
tk.Button(tab_paiements, text="Afficher les Paiements", command=afficher_paiements).pack(pady=10)

# Charger les données au démarrage
afficher_reservations()
afficher_paiements()
afficher_clients()

# Lancer l'application
root.mainloop()
