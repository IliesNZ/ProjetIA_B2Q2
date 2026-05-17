import tkinter as tk
from tkinter import ttk
import threading
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
            break
        
def lancer_processus():

    btn_play.config(state=tk.DISABLED)
    
    barre_chargement.pack(pady=5)
    barre_chargement.start(15) 
    label_statut.config(text="L'IA réfléchit... 🧠")

    def tache_de_fond():
        try:
            iteration()
            label_statut.config(text="Clic effectué !")
        except Exception as e:
            print(f"Erreur: {e}")
            label_statut.config(text="Erreur, voir console")
        finally:
            barre_chargement.stop()
            barre_chargement.pack_forget()
            btn_play.config(state=tk.NORMAL)

    threading.Thread(target=tache_de_fond, daemon=True).start()

root = tk.Tk()
root.title("Bot IA - B2Q2")
root.geometry("250x120")
root.resizable(False, False)

root.attributes('-topmost', True) 

# Le bouton Play
btn_play = tk.Button(root, text="▶ Lancer l'itération", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=lancer_processus)
btn_play.pack(pady=10)

# Le texte d'information
label_statut = tk.Label(root, text="En attente...", font=("Arial", 10))
label_statut.pack()

# La barre de chargement (invisible au démarrage)
barre_chargement = ttk.Progressbar(root, mode='indeterminate', length=180)

if __name__ == "__main__":
    root.mainloop()