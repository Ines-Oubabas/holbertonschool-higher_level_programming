import os

def generate_invitations(template, attendees):
    # Vérifier le type des entrées
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return
    
    # Vérifier si le template est vide
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    # Vérifier si la liste des participants est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Traiter chaque participant
    for index, attendee in enumerate(attendees, start=1):
        # Remplacer les espaces réservés par les valeurs du dictionnaire
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            output = output.replace(f"{{{key}}}", value if value is not None else "N/A")
        
        # Écrire le résultat dans un fichier
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(output)
    
    print(f"{len(attendees)} invitation files generated.")
