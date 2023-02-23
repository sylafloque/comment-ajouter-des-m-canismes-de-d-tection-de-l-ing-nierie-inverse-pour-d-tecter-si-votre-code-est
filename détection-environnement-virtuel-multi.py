#Dans cet exemple, nous utilisons le module platform de Python pour récupérer des informations sur le système d'exploitation. La fonction is_running_in_virtual_environment() retourne True si elle détecte que le programme est exécuté dans un environnement virtuel, sinon elle retourne False.

#Notez que cette méthode n'est pas infaillible et peut être contournée par des outils spécialisés en analyse de code.

import platform

def is_running_in_virtual_environment():
    if platform.system() == "Windows":
        return bool(platform.win32_ver()[0])  # Vérifie la version de Windows
    elif platform.system() == "Linux":
        return bool(platform.linux_distribution()[0])  # Vérifie la distribution Linux
    elif platform.system() == "Darwin":
        return bool(platform.mac_ver()[0])  # Vérifie la version de macOS
    else:
        return False  # Système d'exploitation non pris en charge
