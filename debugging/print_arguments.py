#!/usr/bin/python3
import sys

def print_arguments(arguments):
    """Affiche les arguments passés au script."""
    for index, arg in enumerate(arguments):
        print(f"Argument {index}: {arg}")

if __name__ == "__main__":
    print_arguments(sys.argv)
