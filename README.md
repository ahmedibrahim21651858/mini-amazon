# Mini Amazon Console Application

## Description
This project is a console-based Mini-Amazon system developed in Python.
It simulates a simple e-commerce platform where users can register,
browse products, manage a cart, and place orders.

---

## How to Run the Program

1. Make sure Python 3 is installed.
2. Open a terminal inside the project folder.
3. Run:

python main.py

---

## Features Implemented

- User registration and login system
- Product catalog browsing
- Product search (case-insensitive)
- Shopping cart management
- Checkout system
- Order history
- Persistent storage using JSON files
- Menu-driven console interface
- Input validation and error handling

---

## Project Structure

main.py        → Program entry point  
users.py       → User system  
products.py    → Product catalog  
cart.py        → Shopping cart logic  
orders.py      → Order management  
storage.py     → File storage handler  

---

## Data Storage

The application stores data using JSON files:

- users.json → user accounts
- products.json → product catalog
- carts.json → shopping carts
- orders.json → order history

Data remains saved even after restarting the program.

---

## Known Limitations

- Passwords stored as plain text
- Console interface only (no GUI)
- No admin panel


