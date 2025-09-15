Bank Account Management System

This Python script is a simple console-based program that simulates a bank account management system. It's built using object-oriented programming (OOP) principles to handle customer data and transactions. The program allows users to create a new account, deposit funds, withdraw funds, and check their balance.

Key Features

- Object-Oriented Design: The code uses two classes: Persona and Cliente. Persona is a base class that holds basic information like nombre (name) and apellido (last name), while Cliente inherits from Persona and adds banking-specific attributes like numero_cuenta (account number) and balance. This is a great example of inheritance.

- Encapsulation: The Cliente class encapsulates all the data (attributes) and methods (behaviors) related to a bank client, such as depositar (deposit) and retirar (withdraw). This keeps the code organized and easy to manage.

- User Interface: The program provides a simple, menu-driven interface in the console, guiding the user through the process of creating an account and performing transactions.

- Balance Management: The retirar method includes a check to ensure the user has sufficient funds before allowing a withdrawal, preventing a negative balance.

How to Run the Script

- Save the Code: Save the code into a Python file (e.g., banco.py).

- Open a Terminal: Navigate to the directory where you saved the file.

- Execute: Run the script using the Python interpreter:

      Bash
      
      python banco.py

- Follow the Prompts: The program will ask for your name, last name, and account number. After creating the account, you can choose to deposit, withdraw, or exit the program by typing D, R, or S respectively.

Example Usage

Here is a sample interaction with the program:

    Ingrese su nombre: Juan
    Ingrese su apellido: Perez
    Ingrese su numero de cuenta: 123456
    Cliente: Juan Perez con numero de cuenta: 123456 tiene un saldo de 0
    Elige: Depositar(D), Retirar(R) o Salir(S)
    D
    Monto a depositar: 1000
    Deposito aceptado
    Cliente: Juan Perez con numero de cuenta: 123456 tiene un saldo de 1000
    Elige: Depositar(D), Retirar(R) o Salir(S)
    R
    Monto a retirar: 500
    Retiro realizado
    Cliente: Juan Perez con numero de cuenta: 123456 tiene un saldo de 500
    Elige: Depositar(D), Retirar(R) o Salir(S)
    R
    Monto a retirar: 600
    Fondos insuficientes
    Cliente: Juan Perez con numero de cuenta: 123456 tiene un saldo de 500
    Elige: Depositar(D), Retirar(R) o Salir(S)
    S
    Que tenga un buen dia!!!
