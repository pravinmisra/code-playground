# -*- coding: utf-8 -*-
"""
Created on Fri May 16 23:08:15 2025

@author: Admin
"""

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.1f}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print("Product with this ID already exists.")
        else:
            self.products[product.product_id] = product
            print(f"{product.name} added to inventory. Details below: ")
            print(product)

    def update_quantity(self, product_id, quantity_change):
        if product_id not in self.products:
            print("Product not found.")
        else:
            self.products[product_id].quantity += quantity_change
            print(f"{self.products[product_id].name} quantity updated.")

    def search_product(self, product_id):
        if product_id not in self.products:
            print("Product not found.")
        else:
            print(self.products[product_id])

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for product in self.products.values():
                print(product)


def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Quantity")
        print("3. Search Product")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            product = Product(product_id, name, quantity, price)
            inventory.add_product(product)

        elif choice == '2':
            product_id = input("Enter product ID to update: ")
            quantity_change = int(input("Enter quantity change (positive or negative): "))
            inventory.update_quantity(product_id, quantity_change)

        elif choice == '3':
            product_id = input("Enter product ID to search: ")
            inventory.search_product(product_id)

        elif choice == '4':
            inventory.display_inventory()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
