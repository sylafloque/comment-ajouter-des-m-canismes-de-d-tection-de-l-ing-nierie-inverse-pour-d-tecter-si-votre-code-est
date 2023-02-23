#Voici un exemple de technique Anti-debugging qui consiste à détecter si le programme est en cours de débogage à l'aide du module ptrace sous Linux :

import ctypes

def anti_debug():
    try:
        # Vérifie si le programme est en cours de débogage
        libc = ctypes.CDLL("libc.so.6")
        libc.ptrace(31, 0, 0, 0)
        return False
    except:
        return True

if anti_debug():
    print("Le programme ne peut pas être exécuté sous débogueur.")
    exit(0)

# Code à exécuter normalement si le programme n'est pas en cours de débogage
print("Bonjour, monde !")
