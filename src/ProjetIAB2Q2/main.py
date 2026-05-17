import screen, spotting, extraction

def main():
    iteration()

def iteration():
    capturer_ecran = screen.capturer_ecran()
    print("Analyse de l'image...")

    questions, reponses = spotting.analyser_image(capturer_ecran)
    print("Questions détectées : ", len(questions))
    print("Réponses détectées : ", len(reponses))

    extraction_textes = extraction.extraire_textes(capturer_ecran, questions + reponses)
    print("Textes extraits : ", len(extraction_textes))
    for i, texte in enumerate(extraction_textes):
        print(f"Texte {i+1} : {texte}")

if __name__ == "__main__":
    main()