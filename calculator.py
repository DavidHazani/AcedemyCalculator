import json

# Load the merged study types JSON file
with open('final_database.json', 'r', encoding='utf-8') as file:
    study_data = json.load(file)

def calculate_acceptance_chance(avg_bagrut, avg_pshy, study_type):
    if study_type not in [study["studyType"] for study in study_data]:
        return "Study type not found"
    
    for study in study_data:
        if study["studyType"] == study_type:
            required_avg_bagrut = int(study["avgBagrut"])
            required_avg_pshy = int(study["avgPshy"])

            # Convert Bagrut score to psychometry scale (assuming 1:1 conversion for simplicity)
            converted_bagrut_to_pshy = avg_bagrut

            # Calculate the acceptance score
            acceptance_score = (converted_bagrut_to_pshy + avg_pshy) / 2
            required_score = (required_avg_bagrut + required_avg_pshy) / 2

            # Calculate the percentage
            acceptance_chance = (acceptance_score / required_score) * 100

            # Ensure percentage does not exceed 100%
            acceptance_chance = min(acceptance_chance, 100)

            return round(acceptance_chance, 2)
    
    return "Calculation error"

# Example usage:
avg_bagrut = 98
avg_pshy = 500
study_type = "הנדסת מחשבים"

acceptance_chance = calculate_acceptance_chance(avg_bagrut, avg_pshy, study_type)
print(f'Your acceptance chance for {study_type} is {acceptance_chance}%')
