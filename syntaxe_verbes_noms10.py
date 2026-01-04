import stanza
import os

# Télécharger et initialiser le modèle français de Stanza
stanza.download('fr')
nlp = stanza.Pipeline('fr')

# Chemin du dossier contenant les fichiers
dossier_chunks = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/5月18日projetUNI/chunks"
# Changer la plage pour ne traiter que les 10 premiers fichiers
chemins_fichiers = [
    f"{dossier_chunks}/chunk_{i:03d}.txt"
    for i in range(1, 11)  # Prendre seulement les 10 premiers fichiers
]

# Liste des verbes ciblés
verbes_cibles = [
    "faire", "mettre", "prendre", "tomber", "jeter", "casser", "passer", "jouer",
    "tirer", "donner", "aller", "perdre", "tenir", "tourner", "battre", "baisser",
    "foutre", "pomper", "envoyer", "voir", "lever", "entrer", "laisser", "parler",
    "ouvrir", "couper", "porter", "pousser", "taper"
]

# Listes lexicales
lexiques = {
    "noms": ["ange", "cœur", "flèche", "diable", "salaire", "œufs", "cœur net", "gros", "panier", "ciel", "main"],
    "pronoms": ["y", "en", "les"],
    "objets_directs": ["flèche", "diable", "salaire", "œufs", "cœur net", "vertes", "pas mûres", "gros"],
    "objets_indirects": ["bois", "corps", "panier", "mur", "ciel", "flanc", "vide", "zéro", "patate", "main"],
    "articles": ["la", "le", "les"],
    "adjectifs": ["rouge", "douce", "doux", "bas", "bon", "bien", "froid", "mauvaise"],
    "adverbes": ["bien"],
    "comparaisons": ["comme"]
}

# Liste pour stocker les expressions détectées
expressions_trouvees = []

try:
    for chemin in chemins_fichiers:
        if not os.path.exists(chemin):
            print(f"Fichier introuvable : {chemin}")
            continue

        with open(chemin, 'r', encoding='utf-8') as fichier:
            lignes = fichier.readlines()

        for ligne in lignes:
            phrase = ligne.strip()
            if not phrase:
                continue

            doc = nlp(phrase)

            for phrase_analysee in doc.sentences:
                mots = phrase_analysee.words

                for mot in mots:
                    # Vérification si le mot est un verbe ciblé
                    if mot.upos == "VERB" and mot.lemma.lower() in verbes_cibles:
                        verbe = mot.text
                        id_verbe = mot.id

                        # Chercher les compléments du verbe
                        for autre_mot in mots:
                            if autre_mot.head == id_verbe:  # Complément direct du verbe
                                relation = autre_mot.deprel
                                mot_cible = autre_mot.text.lower()

                                # Vérifier si le mot appartient à un des lexiques
                                for type_lexique, liste_mots in lexiques.items():
                                    if any(mot_cible in entree.lower() for entree in liste_mots):
                                        expression = f"{verbe} {mot_cible}"
                                        
                                        # Filtrage des expressions trop courtes ou non pertinentes
                                        if len(expression.split()) > 1:  # Exclure des expressions comme "faire ce"
                                            expressions_trouvees.append(expression)

    # Éliminer les doublons et trier
    expressions_uniques = sorted(set(expressions_trouvees))

    # Écriture dans le fichier de sortie
    chemin_sortie = "/Users/lianchen/Desktop/拉脱维亚-6月26-28/5月18日projetUNI/verbe_noms10.txt"
    with open(chemin_sortie, "w", encoding="utf-8") as fichier_sortie:
        fichier_sortie.write("Unités phraséologiques détectées :\n")
        for exp in expressions_uniques:
            fichier_sortie.write(exp + "\n")

    print("✔ Les unités phraséologiques ont été enregistrées dans verbe_noms10.txt")

except Exception as e:
    print(f" Une erreur est survenue : {e}")

#结果一个一个地输出
# d /Users/lianchen/Desktop/拉脱维亚-口语6月27日/5月18日projetUNI/
# Créer l'environnement avec ton python 3.12
#/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv stanza_env
#source stanza_env/bin/activate
#pip install stanza
#python verbes_ameliore_10.py