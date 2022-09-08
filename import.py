import requests
import json
import unicodedata


open_quizz_db_data = (
    ("Animaux", "Animaux en vrac", "https://www.kiwime.com/oqdb/files/2184923922/OpenQuizzDB_184/openquizzdb_184.json"),
    ("Culture générale", "Culture en vrac", "https://www.kiwime.com/oqdb/files/2187579277/OpenQuizzDB_187/openquizzdb_187.json"),
    ("Comic", "Tintin", "https://www.kiwime.com/oqdb/files/2124242395/OpenQuizzDB_124/openquizzdb_124.json"),
)


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def get_quizz_filename(categorie, titre, difficulte):
    return strip_accents(categorie).lower().replace(" ", "") + "_" + strip_accents(titre).lower().replace(" ", "") + "_" + strip_accents(difficulte).lower().replace(" ", "") + ".json"


def generate_json_file(categorie, titre, url):
    out_questionnaire_data = {"categorie": categorie, "titre": titre, "questions": []}
    out_questions_data = []
    try:
        response = requests.get(url)
    except:
        print(f"Exeception pour l'url: {url}")
    else:
        try:
            data = json.loads(response.text)
            all_quizz = data["quizz"]["fr"]
            for quizz_title, quizz_data in all_quizz.items():
                out_filename = get_quizz_filename(categorie, titre, quizz_title)
                print(out_filename)
                out_questionnaire_data["difficulte"] = quizz_title
                for question in quizz_data:
                    question_dict = {}
                    question_dict["titre"] = question["question"]
                    question_dict["choix"] = []
                    for ch in question["propositions"]:
                        question_dict["choix"].append((ch, ch==question["réponse"]))
                    out_questions_data.append(question_dict)
                out_questionnaire_data["questions"] = out_questions_data
                out_json = json.dumps(out_questionnaire_data)

                file = open(out_filename, "w")
                file.write(out_json)
                file.close()
                print("end")
        except:
            print(f"Exeception data pour {titre} avec l'url: {url}")
    


for quizz_data in open_quizz_db_data:
    generate_json_file(quizz_data[0], quizz_data[1], quizz_data[2])

