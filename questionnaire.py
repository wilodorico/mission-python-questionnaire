import json

questionnaire = open("animaux_animauxenvrac_debutant.json")
questionnaire_json = json.load(questionnaire)

class Question:
    def __init__(self, titre, choix):
        self.titre = titre
        self.choix = choix

    def poser(self):
        print()
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i][0])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1][1] == True:
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    

class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        num_question = 0
        print()
        print(f"Titre : {self.questions['titre']}")
        print(f"Catégorie : {self.questions['categorie']}")
        print(f"Niveau : {self.questions['difficulte']}")
        print(f"Total : {len(self.questions['questions'])} questions")
        print()

        for question in self.questions["questions"]:
            num_question += 1
            print(f"n°{num_question}/{len(self.questions['questions'])} :")
            q = Question(question['titre'], question['choix'])
            if q.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions['questions']))
        print()
        return score
    

Questionnaire(
    questionnaire_json
).lancer()
