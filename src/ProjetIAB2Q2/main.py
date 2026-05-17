import screen, spotting, extraction, prompt, click

def main():
    iteration()

def iteration():
    capturer_ecran = screen.capturer_ecran()
    print("Analyse de l'image...")

    questions, reponses = spotting.analyser_image(capturer_ecran)
    print("Questions détectées : ", len(questions), " : ", questions)
    print("Réponses détectées : ", len(reponses), " : ", reponses)

    question_textes, reponses_textes = extraction.extraire_textes(capturer_ecran, questions + reponses)
    print("Question extraite : ", question_textes)
    print("Réponses extraites : ", reponses_textes)

    reponse = prompt.trouver_bonne_reponse(question_textes, reponses_textes)
    print("Réponse trouvée : ", reponse)

    for i in range(4):
        if reponse == reponses_textes[i]:
            print(f"Coordonnées de la réponse : {reponses[i]}")
            click.click_on_answer(reponses[i])
            continue



if __name__ == "__main__":
    main()