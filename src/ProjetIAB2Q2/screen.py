import os
import time
import pyautogui


def capturer_ecran():
    print("Préparation de la capture d'écran...")
    
    print("Capture dans 2 secondes...")
    time.sleep(2)
    
    dossier_images = "images"
    if not os.path.exists(dossier_images):
        os.makedirs(dossier_images)
        
    #supprimer les anciennes captures d'écran
    for fichier in os.listdir(dossier_images):
        chemin_fichier = os.path.join(dossier_images, fichier)
        if os.path.isfile(chemin_fichier):
            os.remove(chemin_fichier)
    
    # Nom du fichier de sauvegarde
    chemin_sauvegarde = os.path.join(dossier_images, "image.png")
    
    # Capture et sauvegarde magique
    screenshot = pyautogui.screenshot()
    screenshot.save(chemin_sauvegarde)
    
    print(f"Capture d'écran enregistrée avec succès sous : {chemin_sauvegarde}")
    return chemin_sauvegarde