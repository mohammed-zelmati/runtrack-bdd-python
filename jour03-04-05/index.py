import tkinter as tk
from tkinter import ttk, messagebox
import csv
import mysql.connector

# Connexion à MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="357321zM@.",
    database="store"
)
cursor = conn.cursor()

# Fenêtre principale
root = tk.Tk()
root.title("Gestion de stock")

# Liste des produits
def afficher_produits():
    cursor.execute("SELECT * FROM product")
    produits = cursor.fetchall()
    for item in tableau.get_children():
        tableau.delete(item)
    for produit in produits:
        tableau.insert("", "end", values=produit)

def ajouter_produit():
    # Ajouter un produit (nom, description, prix, quantité, id catégorie)
    name = entry_name.get()
    description = entry_description.get()
    price = int(entry_price.get())
    quantity = int(entry_quantity.get())
    id_category = int(entry_category.get())
    cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                   (name, description, price, quantity, id_category))
    conn.commit()
    afficher_produits()

# Modifier un produit
def modifier_produit():
    selected_item = tableau.selection()  # Obtenez l'élément sélectionné
    if not selected_item:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner un produit à modifier.")
        return

    values = tableau.item(selected_item[0], "values")  # Obtenez les données du produit
    product_id = values[0]  # L'ID du produit est dans la première colonne

    # Afficher une fenêtre pour modifier les informations
    modif_window = tk.Toplevel(root)
    modif_window.title("Modifier le produit")

    # Champs pour modification
    tk.Label(modif_window, text="Nom").grid(row=0, column=0)
    modif_name = tk.Entry(modif_window)
    modif_name.grid(row=0, column=1)
    modif_name.insert(0, values[1])  # Nom existant

    tk.Label(modif_window, text="Description").grid(row=1, column=0)
    modif_description = tk.Entry(modif_window)
    modif_description.grid(row=1, column=1)
    modif_description.insert(0, values[2])  # Description existante

    tk.Label(modif_window, text="Prix").grid(row=2, column=0)
    modif_price = tk.Entry(modif_window)
    modif_price.grid(row=2, column=1)
    modif_price.insert(0, values[3])  # Prix existant

    tk.Label(modif_window, text="Quantité").grid(row=3, column=0)
    modif_quantity = tk.Entry(modif_window)
    modif_quantity.grid(row=3, column=1)
    modif_quantity.insert(0, values[4])  # Quantité existante

    tk.Label(modif_window, text="ID Catégorie").grid(row=4, column=0)
    modif_category = tk.Entry(modif_window)
    modif_category.grid(row=4, column=1)
    modif_category.insert(0, values[5])  # ID catégorie existant

    # Enregistrer les modifications
    def sauvegarder_modifications():
        new_name = modif_name.get()
        new_description = modif_description.get()
        new_price = int(modif_price.get())
        new_quantity = int(modif_quantity.get())
        new_category = int(modif_category.get())

        cursor.execute("""
        UPDATE product
        SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s
        WHERE id = %s
        """, (new_name, new_description, new_price, new_quantity, new_category, product_id))
        conn.commit()
        messagebox.showinfo("Succès", "Le produit a été modifié avec succès.")
        modif_window.destroy()
        afficher_produits()

    tk.Button(modif_window, text="Enregistrer", command=sauvegarder_modifications).grid(row=5, column=1)

    
# Supprimer un ou plusieurs produits
def supprimer_produit():
    selected_items = tableau.selection()  # Obtenez les éléments sélectionnés
    if not selected_items:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner un produit à supprimer.")
        return

    confirm = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer les produits sélectionnés ?")
    if not confirm:
        return

    for item in selected_items:
        values = tableau.item(item, "values")  # Obtenez les données du produit
        product_id = values[0]  # L'ID du produit est dans la première colonne
        cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
        conn.commit()
        tableau.delete(item)  # Supprimez l'élément du tableau

    messagebox.showinfo("Succès", "Le(s) produit(s) ont été supprimé(s) avec succès.")
    afficher_produits()


# Tableau des produits
tableau = ttk.Treeview(root, columns=("id", "name", "description", "price", "quantity", "id_category"), show="headings")
for col in tableau["columns"]:
    tableau.heading(col, text=col)
tableau.pack()

# Formulaire pour ajouter un produit
frame_form = tk.Frame(root)
frame_form.pack()

tk.Label(frame_form, text="Nom").grid(row=0, column=0)
entry_name = tk.Entry(frame_form)
entry_name.grid(row=0, column=1)

tk.Label(frame_form, text="Description").grid(row=1, column=0)
entry_description = tk.Entry(frame_form)
entry_description.grid(row=1, column=1)

tk.Label(frame_form, text="Prix").grid(row=2, column=0)
entry_price = tk.Entry(frame_form)
entry_price.grid(row=2, column=1)

tk.Label(frame_form, text="Quantité").grid(row=3, column=0)
entry_quantity = tk.Entry(frame_form)
entry_quantity.grid(row=3, column=1)

tk.Label(frame_form, text="ID Catégorie").grid(row=4, column=0)
entry_category = tk.Entry(frame_form)
entry_category.grid(row=4, column=1)

tk.Button(frame_form, text="Ajouter", command=ajouter_produit).grid(row=5, column=1)

# Charger les produits au démarrage
afficher_produits()

tk.Button(root, text="Modifier le produit", command=modifier_produit).pack(pady=10)

# Bouton pour supprimer un produit
tk.Button(root, text="Supprimer le produit", command=supprimer_produit).pack(pady=10)

root.mainloop()
