# Utilisation de CNN pour récupérer la question et ses réponses
# Utilisation de Roboflow pour faire du spotting de texte sur les images de quiz Cisco
# pip install ultralytics

from ultralytics import YOLO

# 1. On charge un modèle pré-entraîné très léger ('n' pour nano)
# Ça lui évite de devoir apprendre ce qu'est une ligne ou un pixel en partant de zéro
model = YOLO('yolov8n.pt') 

if __name__ == '__main__':
    # 2. On lance l'entraînement sur ton dataset de quiz Cisco
    print("Démarrage de l'entraînement du CNN...")
    
    results = model.train(
        data='dataset_roboflow/data.yaml',      # Chemin vers le dataset
        epochs=30,                              # Le nombre de fois qu'il va revoir le dataset
        imgsz=512,                              # La taille des images 
        plots=True                              # Générer un graphique de l'entraînement
    )
    
    print("Entraînement terminé ! Le modèle est sauvegardé.")
