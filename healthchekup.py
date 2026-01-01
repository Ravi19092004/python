rules = [
    {
        "if": {"fever": True, "cough": True, "shortness of breath": True},
        "then": {"disease": "COVID-19"}
    },
    {
        "if": {"fever": True, "rash": True, "joint pain": False},
        "then": {"disease": "Dengue"}
    },
    {
        "if": {"fever": True, "cough": False, "sore throat": False},
        "then": {"disease": "Influenza"}
    }
]

def diagnose(symptoms):
    for rule in rules:
        if all(symptoms.get(key) == value for key, value in rule["if"].items()):
            return rule["then"]["disease"]
    return "Unknown Disease"

def get_symptoms():
    symptoms = {}
    symptoms["fever"] = input("Do you have fever? (yes/no): ").strip().lower() == "yes"
    symptoms["cough"] = input("Do you have cough? (yes/no): ").strip().lower() == "yes"
    symptoms["shortness of breath"] = input("Do you have shortness of breath? (yes/no): ").strip().lower() == "yes"
    symptoms["rash"] = input("Do you have rash? (yes/no): ").strip().lower() == "yes"
    symptoms["joint pain"] = input("Do you have joint pain? (yes/no): ").strip().lower() == "yes"
    symptoms["sore throat"] = input("Do you have sore throat? (yes/no): ").strip().lower() == "yes"
    return symptoms

def main():
    print("Welcome to the Medical Diagnosis System!")
    symptoms = get_symptoms()
    disease = diagnose(symptoms)
    print(f"You have disease: {disease}")

if __name__ == "main":
    main()

# Test cases
test_symptoms1 = {"fever": True, "cough": True, "shortness of breath": True}
test_symptoms2 = {"fever": True, "rash": True, "joint pain": False}
test_symptoms3 = {"fever": False, "cough": False, "sore throat": False}

print(diagnose(test_symptoms1)) 
print(diagnose(test_symptoms2)) 
print(diagnose(test_symptoms3))