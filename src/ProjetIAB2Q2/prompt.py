# pip install ollamaimport ollama

import ollama

def trouver_bonne_reponse(question, liste_reponses):

    print("Réflexion de Qwen en cours...")
    
    prompt = f"""
Je vais te donner une question et une liste de choix.
Tu dois répondre UNIQUEMENT en recopiant le texte exact de la bonne réponse parmi les choix proposés. 
Ne donne aucune explication, aucune introduction. Juste la réponse.

Question : {question}

Choix :
"""
    for rep in liste_reponses:
        prompt += f"- {rep}\n"

    reponse_api = ollama.chat(model='nemotron-3-super:cloud', messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ])

    texte_ia = reponse_api['message']['content'].strip()     # Nettoyage de la reponse

    return texte_ia