# Permet d'extraire le texte des boites
# pip install easyocr

import easyocr
import cv2

print("Chargement du modèle OCR en cours...")
lecteur = easyocr.Reader(['fr', 'en'])

def extraire_textes(chemin_image_globale, coordonnees_boites):
    image = cv2.imread(chemin_image_globale)
    textes_lus = []

    for (x1, y1, x2, y2) in coordonnees_boites:

        zone_decoupee = image[y1:y2, x1:x2]
        mots_trouves = lecteur.readtext(zone_decoupee, detail=0)

        phrase_complete = " ".join(mots_trouves)
        textes_lus.append(phrase_complete)

    return textes_lus

if __name__ == '__main__':
    print("Le module d'extraction est prêt à être importé !")

