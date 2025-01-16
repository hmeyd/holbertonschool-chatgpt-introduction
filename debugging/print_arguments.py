!/usr/bin/python3
import sys
# Vérifie si des arguments ont été passés
if len(sys.argv) > 1:
    # Parcourt les arguments en ignorant le nom du script
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
else:
    print("Aucun argument n'a été fourni.")
