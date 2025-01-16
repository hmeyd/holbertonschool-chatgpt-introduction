#!/usr/bin/python3
import sys

def factorial(n):
    """Calcule récursivement la factorielle d'un nombre entier positif."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        # Vérifie que l'argument est bien un entier non négatif
        if len(sys.argv) != 2:
            print("Usage: ./factorial_recursive.py <non-negative integer>")
            return

        n = int(sys.argv[1])
        if n < 0:
            print("Veuillez entrer un entier non négatif.")
            return

        print(factorial(n))

    except ValueError:
        print("Erreur : L'argument doit être un entier.")

if __name__ == "__main__":
    main()
