# E-Commerce Console Application

## Author Information
Name: Emre Sonkaya
Student ID: 100007503


## Description
This project is a console-based e-commerce application built with Python. It features a complete object-oriented design and uses JSON files for local data storage. The system allows users to register, log in, browse products, manage a shopping cart, and complete purchases with real-time stock updates.

## Features
- User Authentication: Secure registration and login system.
- Product Management: View and search the product catalog.
- Shopping Cart: Add items, update quantities, and remove items with real-time stock validation.
- Checkout System: Process payments, update product stock in the database, and generate order receipts.
- Order History: View past purchases.
- Persistent Storage: All data is saved locally using JSON files.

## Project Structure
- main.py: The entry point of the application containing the interactive menus.
- storage.py: Handles reading from and writing to JSON files.
- users.py: Manages user registration, authentication, and session state.
- products.py: Manages the product catalog, search functionality, and stock levels.
- cart.py: Handles shopping cart operations and validations.
- orders.py: Processes checkout, generates receipts, and stores order history.
- .json files: Data storage files (users.json, products.json, carts.json, orders.json).

## How to Run
1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the command: python main.py

## Dependencies
This project strictly uses Python built-in libraries (json, os, datetime, random). No external packages or installations are required.
