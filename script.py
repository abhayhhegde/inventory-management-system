import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

# Global variables for entry widgets and listbox
entry_item_name = None
entry_quantity = None
entry_price = None
entry_item_id = None
inventory_listbox = None

# Function to create the inventory table
def create_table():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS inventory (
                item_id INTEGER PRIMARY KEY,
                item_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
                )''')
    conn.commit()
    conn.close()

# Function to add an item to the inventory
def add_item():
    item_name = entry_item_name.get()
    quantity = int(entry_quantity.get())
    price = float(entry_price.get())

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''INSERT INTO inventory (item_name, quantity, price) 
                VALUES (?, ?, ?)''', (item_name, quantity, price))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Item added to inventory!")
    entry_item_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    display_inventory()

# Function to update an item's quantity and price
def update_item():
    item_id = int(entry_item_id.get())
    quantity = int(entry_quantity.get())
    price = float(entry_price.get())

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''UPDATE inventory SET quantity=?, price=? WHERE item_id=?''', (quantity, price, item_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Item updated!")
    entry_item_id.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    display_inventory()

# Function to delete an item from the inventory
def delete_item():
    item_id = int(entry_item_id.get())

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''DELETE FROM inventory WHERE item_id=?''', (item_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Item deleted!")
    entry_item_id.delete(0, tk.END)
    display_inventory()

# Function to retrieve all items from the inventory
def get_all_items():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM inventory''')
    items = c.fetchall()
    conn.close()
    return items

# Function to display the current inventory in the listbox
def display_inventory():
    inventory_listbox.delete(0, tk.END)
    items = get_all_items()
    for item in items:
        inventory_listbox.insert(tk.END, f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}, Price: {item[3]}")

# Main function to create the GUI
def main():
    create_table()
    homepage.destroy()
    global entry_item_name, entry_quantity, entry_price, entry_item_id, inventory_listbox
    
    root = tk.Tk()
    root.title("Inventory Management App") 
    # Labels and Entry widgets for adding items
    label_item_name = tk.Label(root, text="Item Name:")
    label_item_name.grid(row=0, column=0, padx=5, pady=5)
    entry_item_name = tk.Entry(root)
    entry_item_name.grid(row=0, column=1, padx=5, pady=5)

    label_quantity = tk.Label(root, text="Quantity:")
    label_quantity.grid(row=0, column=2, padx=5, pady=5)
    entry_quantity = tk.Entry(root)
    entry_quantity.grid(row=0, column=3, padx=5, pady=5)

    label_price = tk.Label(root, text="Price:")
    label_price.grid(row=0, column=4, padx=5, pady=5)
    entry_price = tk.Entry(root)
    entry_price.grid(row=0, column=5, padx=5, pady=5)

    # Buttons for adding and updating items
    btn_add_item = tk.Button(root, text="Add Item", command=add_item)
    btn_add_item.grid(row=0, column=6, padx=5, pady=5)
    changeonhover(btn_add_item,"grey","lightgrey")
    label_item_id = tk.Label(root, text="Item ID:")
    label_item_id.grid(row=1, column=0, padx=5, pady=5)
    entry_item_id = tk.Entry(root)
    entry_item_id.grid(row=1, column=1, padx=5, pady=5)

    btn_update_item = tk.Button(root, text="Update Item", command=update_item)
    btn_update_item.grid(row=1, column=2, padx=5, pady=5)
    changeonhover(btn_update_item,"grey","lightgrey")
    # Button for deleting an item
    btn_delete_item = tk.Button(root, text="Delete Item", command=delete_item)
    btn_delete_item.grid(row=1, column=3, padx=5, pady=5)
    changeonhover(btn_delete_item,"grey","lightgrey")
    # Listbox to display the current inventory
    inventory_listbox = tk.Listbox(root, width=70, height=10)
    inventory_listbox.grid(row=2, column=0, columnspan=7, padx=5, pady=5)

    # Display the current inventory
    display_inventory()
    root.mainloop()
def changeonhover(but,conh,conl):
    but.bind('<Enter>',func=lambda e:but.config(background=conh))
    but.bind('<Leave>',func=lambda e:but.config(background=conl))

if __name__ == '__main__':
    homepage=tk.Tk()
    homepage.geometry("300x300")
    
    Label(homepage,text="YOUR INVENTORY MANAGER ",font="bellgothic 12 bold").pack(pady=10)
    
    start_button=Button(homepage,text="Start",command=main,width=20,height=2,bg="lightgrey")
    start_button.place(x=75,y=115)
    changeonhover(start_button,"grey","lightgrey")
    homepage.mainloop()
    # main()
