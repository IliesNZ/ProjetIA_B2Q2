# Utilisation de CNN pour récupérer la question et ses réponses
# Utilisation de Roboflow pour faire du spotting de texte sur les images de quiz Cisco
# pip install ultralytics pour utiliser le modèle de CNN YOLOv8s

from ultralytics import YOLO

model = YOLO('yolov8s.pt') # modele de CNN que l'on va entrainer 

if __name__ == '__main__':
    print("Démarrage de l'entraînement du CNN...")
    
    results = model.train(
        data='dataset_roboflow/data.yaml',      # Chemin vers le dataset
        epochs=30,                              # Le nombre de fois qu'il va revoir le dataset
        imgsz=640,                              # La taille des images 
        plots=True                              # Générer un graphique de l'entraînement
    )
    
    print("Entraînement terminé ! Le modèle est sauvegardé.")