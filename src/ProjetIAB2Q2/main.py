import screen, spotting, extraction, prompt

def main():
    iteration()

def iteration():
    capturer_ecran = screen.capturer_ecran()
    print("Analyse de l'image...")

    questions, reponses = spotting.analyser_image(capturer_ecran)
    print("Questions détectées : ", len(questions))
    print("Réponses détectées : ", len(reponses))

    question_textes, reponses_textes = extraction.extraire_textes(capturer_ecran, questions + reponses)
    print("Question extraite : ", question_textes)
    print("Réponses extraites : ", reponses_textes)

    reponse = prompt.trouver_bonne_reponse(question_textes, reponses_textes)
    print("Réponse trouvée : ", reponse)

if __name__ == "__main__":
    main()