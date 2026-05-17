import screen, spotting

def main():
    capturer_ecran = screen.capturer_ecran()
    print("Analyse de l'image...")

    questions, reponses = spotting.analyser_image(capturer_ecran)
    print("Questions détectées : ", len(questions))
    print("Réponses détectées : ", len(reponses))

if __name__ == "__main__":
    main()