# pip install ollamaimport ollama

import os
import ollama

def charger_tous_les_cours(nom_dossier="md"):
    texte_global = ""
    
    dossier_script = os.path.dirname(os.path.abspath(__file__))
    chemin_dossier = os.path.join(dossier_script, nom_dossier)
    
    if not os.path.exists(chemin_dossier):
        print(f"Dossier introuvable au chemin : {chemin_dossier}")
        return ""

    print(f"Dossier Markdown trouvé !")
    for nom_fichier in os.listdir(chemin_dossier):
        if nom_fichier.endswith(".md"):  # On ne prend que les fichiers Markdown
            chemin_fichier = os.path.join(chemin_dossier, nom_fichier)
            with open(chemin_fichier, "r", encoding="utf-8") as f:
                texte_global += f"\n\n--- DOCUMENT : {nom_fichier} ---\n\n"
                texte_global += f.read()
                
    return texte_global

def trouver_bonne_reponse(question, liste_reponses):

    antiseche_geante = charger_tous_les_cours("md")

    print("Réflexion de Qwen en cours...")
    
    prompt = f"""
Aide toi de cette antisèche géante pour trouver la bonne réponse :
{antiseche_geante}

Je vais te donner une question et une liste de choix.
Tu dois répondre UNIQUEMENT en recopiant le texte exact de la bonne réponse parmi les choix proposés. 
Trouve la bonne réponse parmi les choix proposés. Tu dois répondre UNIQUEMENT en recopiant le texte exact de la bonne réponse. Zéro explication. Zéro texte avant ou après.

Question : {question}

Choix :
"""
    for rep in liste_reponses:
        prompt += f"- {rep}\n"

    reponse_api = ollama.chat(model='llama3.1', messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ])

    texte_ia = reponse_api['message']['content'].strip()     # Nettoyage de la reponse

    return texte_ia