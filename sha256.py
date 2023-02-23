# L'anti-tampering est une technique de sécurité pour protéger votre code contre la modification ou la manipulation. Voici un exemple simple en Python pour détecter si le fichier de votre code a été modifié :

import hashlib

# Calculer le hash du fichier original
with open('mon_script.py', 'rb') as f:
    original_hash = hashlib.sha256(f.read()).hexdigest()

# Vérifier si le hash du fichier a changé
with open('mon_script.py', 'rb') as f:
    current_hash = hashlib.sha256(f.read()).hexdigest()
if current_hash != original_hash:
    print("Le fichier a été modifié !")

# Dans cet exemple, nous calculons le hash SHA256 du fichier original et le stockons dans la variable original_hash. Ensuite, nous comparons le hash du fichier actuel avec le hash original. Si le hash a changé, cela signifie que le fichier a été modifié et nous affichons un message d'erreur.

# Cette technique peut être améliorée en stockant le hash original dans un fichier ou dans une base de données distante, afin que l'attaquant ne puisse pas simplement modifier le hash original stocké sur la même machine.
