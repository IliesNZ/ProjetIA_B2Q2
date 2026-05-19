# pip install ollamaimport ollama

import os
import ollama

def trouver_bonne_reponse(question, liste_reponses):

    print("Réflexion de Qwen en cours...")
    
    prompt = f"""

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