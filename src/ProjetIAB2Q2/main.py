import screen, spotting, extraction, prompt, click
from ui import MinimalUI

def iteration():

    print(f"Capture d'écran dans 2 secondes... \n")
    capturer_ecran = screen.capturer_ecran()

    print("CNN en cours d'analyse de l'image... \n")
    questions, reponses = spotting.analyser_image(capturer_ecran)
    print("Questions détectées : ", len(questions), " : ", questions)
    print("Réponses détectées : ", len(reponses), " : ", reponses)

    print("CRNN en cours d'analyse... \n")
    question_textes, reponses_textes = extraction.extraire_textes(capturer_ecran, questions + reponses)
    print("Question extraite : ", question_textes)
    print("Réponses extraites : ", reponses_textes)

    print("Transformer en cours de traitement... \n")
    reponse = prompt.trouver_bonne_reponse(question_textes, reponses_textes)
    print("Réponse trouvée : ", reponse)

    print("Clic en cours... \n")
    for i in range(len(reponses_textes)):
        print(f"Comparaison entre : '{reponse}' et '{reponses_textes[i]}'")
        if reponse == reponses_textes[i]:
            print(f"Coordonnées de la réponse : {reponses[i]}")
            click.click_on_answer(reponses[i])
            break

if __name__ == "__main__":
    ui = MinimalUI(on_play_callback=iteration)
    ui.run()