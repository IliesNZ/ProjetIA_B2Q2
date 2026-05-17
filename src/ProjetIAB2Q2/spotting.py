from ultralytics import YOLO
from PIL import Image

PATH_MODEL = '../../runs/detect/train-2/weights/best.pt'
model = YOLO(PATH_MODEL)

def recadrage_ecran(chemin_screenshot):
    img = Image.open(chemin_screenshot)
    largeur, hauteur = img.size
    
    left = int(largeur * 0.20)   
    top = int(hauteur * 0.02)    
    right = int(largeur * 0.85)  
    bottom = int(hauteur * 0.90) 
    
    img_crop = img.crop((left, top, right, bottom))
    chemin_crop = "images/image_zoom.png"
    img_crop.save(chemin_crop)
    
    return chemin_crop, left, top

def analyser_image(path_image_globale):

    image_zoom, offset_x, offset_y = recadrage_ecran(path_image_globale)   #Zoom pour aider l'IA
    
    resultats = model.predict(
        source=image_zoom, 
        conf=0.35,              # On remonte la confiance à 40% pour éliminer les faux rectangles vides
        imgsz=640,              # Taille de l'image 
        iou=0.25,               # Si deux boites se touchent => elles fusionnent
        agnostic_nms=True,      # Force le nettoyage des boîtes même si l'IA hésite entre la classe question/réponse
        save=True               # Capture les résultats
    )   
    
    boites = resultats[0].boxes                     #récupère les coorendées des boîtes détectées
    questions_trouvees = []
    reponses_trouvees = []

    largeur_image = resultats[0].orig_img.shape[1]

    for boite in boites:
        x1, y1, x2, y2 = boite.xyxy[0].tolist()     # Récupère les coordonnées 

        if x1 < (largeur_image * 0.10):             # Supprime la liste à gauche 
            continue

        id_classe = int(boite.cls[0].item())        # Récupère la classe
        nom_classe = model.names[id_classe]

        vrai_x1 = int(x1) + offset_x                # Puisque l'image a été recadrée, on doit réajuster les coordonnées
        vrai_y1 = int(y1) + offset_y                # offset représente le decalage 
        vrai_x2 = int(x2) + offset_x
        vrai_y2 = int(y2) + offset_y

        coordonnees = (vrai_x1, vrai_y1, vrai_x2, vrai_y2)

        if nom_classe == 'question':
            questions_trouvees.append(coordonnees)
        elif nom_classe == 'reponse':
            reponses_trouvees.append(coordonnees)

    return questions_trouvees, reponses_trouvees

if __name__ == '__main__':
    IMAGE = "images/image.png" 
    questions, reponses = analyser_image(IMAGE)