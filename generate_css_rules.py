import csv
import os

def generate_css_rules():
    # Chemin du fichier CSV
    csv_file = 'csv/clubdeal.csv'
    # Chemin du fichier CSS de sortie
    output_file = 'generated_rules.css'

    # Vérifier si le fichier CSV existe
    if not os.path.exists(csv_file):
        print(f"Erreur: Le fichier {csv_file} n'existe pas.")
        return

    # Lire le CSV et générer les règles CSS
    css_rules = []
    with open(csv_file, 'r') as f:
        csv_reader = csv.DictReader(f)
        print("Contenu du CSV :")
        for row in csv_reader:
            userid = row['userid']
            projectid = row['projectid']
            print(f"Lecture de la ligne - userid: {userid}, projectid: {projectid}")

            # Générer la règle CSS
            css_rule = f"""body:has(#desktop_default_client_space[href="/fr/users/{userid}/edit"])
  #box_project_{projectid} {{
    display: block !important;
  }}"""
            css_rules.append(css_rule)
            print(f"Règle CSS générée :\n{css_rule}\n")

    # Écrire les règles dans le fichier CSS
    with open(output_file, 'w') as f:
        f.write('\n\n'.join(css_rules))

    print(f"Les règles CSS ont été générées dans le fichier {output_file}")
    print(f"Nombre total de règles générées : {len(css_rules)}")

if __name__ == "__main__":
    generate_css_rules()