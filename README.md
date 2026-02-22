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

## Known limitations

- No real payment processing → checkout simulates orders without actual transactions
- Console-based interface → the application runs only in the terminal and does not provide a graphical or web interface
- Single-user execution → the program assumes only one user is running it at a time
- No admin management interface → products must be edited manually in products.json





