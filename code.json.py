import json
import re

# Load your large JSON from a file (replace 'large_data.json' with your filename)
with open('large_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Function to sanitize filenames safely
def sanitize_filename(name):
    return re.sub(r'\W+', '_', name.strip().lower())

# Loop over each disease entry (element) in the JSON array
for entry in data:
    # Each entry is a dictionary with one key as the disease name, get it:
    disease_name = list(entry.keys())[0]
    # Get the corresponding data object
    disease_data = entry[disease_name]

    # Create a filename from the disease name
    filename = sanitize_filename(disease_name) + '.json'

    # Write out this disease's data to its own JSON file
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump({disease_name: disease_data}, outfile, indent=2)

    print(f'Saved {filename}')


[
{"Acute Clinical Mastitis": {
    "keywords": ["Inflammation of the teat", "fever above 39 C", "weak and dejected animal", "lack of appetite", "Drastic drop in milk yield"],
    "diagnosis": "Likely Acute Clinical Mastitis",
    "treatment": "Milk out gently 3x/day; Mix 1 teaspoon turmeric powder in 1 cup of clean warm water and use as a teat dip after milking; warm compress and udder washing with proper hygine; Dry and keep udder clean with clean cloth and consistently wash your hands; clean bedding and attempt to neutralize temprature; if condition worsens take antibiotics per reccomendation"},
  
   "disease": "Foot-and-Mouth Disease (FMD)",
  "treatment_protocol": {
    "isolation": {
      "steps": [
        "Separate sick animals from healthy ones.",
        "Disinfect sheds, tools, and footwear with lime or bleaching powder."
      ]
    },
    "supportive_care": {
      "steps": [
        "Provide soft, easily digestible feed (bran mash, green fodder, gruels).",
        "Ensure plenty of clean drinking water.",
        "Avoid rough fodder that irritates mouth ulcers."
      ]
    },
    "mouth_lesions": {
      "steps": [
        "Wash mouth with antiseptic solution (1:1000 potassium permanganate, alum, or borax solution).",
        "Apply soothing agents (glycerin or coconut oil)."
      ]
    },
    "foot_lesions": {
      "steps": [
        "Wash hooves with 1% potassium permanganate or copper sulfate solution.",
        "Apply antiseptic ointments (zinc oxide, boric acid, neem or turmeric paste).",
        "Keep animals on dry ground."
      ]
    },
    "secondary_infections": {
      "steps": [
        "Administer broad-spectrum antibiotics (penicillin, streptomycin, or oxytetracycline).",
        "Give NSAIDs or paracetamol to reduce fever and pain."
      ]
    },
    "vaccination": {
      "steps": [
        "Vaccinate cattle, buffalo, sheep, goats, and pigs twice a year with trivalent FMD vaccine.",
        "Maintain cold chain for vaccine storage."
      ]
    }
  },
  "notes": [
    "No direct cure exists for FMD; treatment is supportive.",
    "Prevention through vaccination is the most effective long-term strategy.",
    "Traditional remedies (neem, turmeric, mustard oil) can help but should not replace vaccination."
  ]}
  


  ,
{
  "Hyperacute Clinical Mastitis":null}, {
    "keywords": ["Swollen", "red", "painful quarter","Milk passes with difficulty", "Fever over 41 C", "Cow has no appetite", "shivers and loses weight quickly", "Lactation often stops."],
    "diagnosis": "Likely Hyperacute Clinical Mastitis",
    "treatment": "Milk out gently 3x/day; Mix 1 teaspoon turmeric powder in 1 cup of clean warm water and use as a teat dip after milking; warm compress and udder washing with proper hygine; Dry and keep udder clean with clean cloth and consistently wash your hands; clean bedding and attempt to neutralize temprature; if condition worsens take antibiotics per reccomendation."
  },
{
  "Subacute Clinical Mastitis": {
    "keywords": "No apparent change in udder, presence of flaky particles in milk, especially in initial ejection. Subject appears healthy.]",
    "diagnosis": "Likely Hyperacute Clinical Mastitis",
    "treatment": "Milk out gently 3x/day; Mix 1 teaspoon turmeric powder in 1 cup of clean warm water and use as a teat dip after milking; warm compress and udder washing with proper hygine; Dry and keep udder clean with clean cloth and consistently wash your hands; clean bedding and attempt to neutralize temprature;if condition worsens take antibiotics per reccomendation"
  }},
  
  {
  "Chronic Mastitis": {
    "keywords": ["Repeated but mild clinical attacks", "generally without fever", "Lumpy milk", "quarters sometimes swollen", "Quarter may become hard (fibrous indurations)", "Antibiotic treatments often do not work"],
    "diagnosis": "Likely Chronic Mastitis",
    "treatment\";":"Milk out gently 3x/day; Mix 1 teaspoon turmeric powder in 1 cup of clean warm water and use as a teat dip after milking; warm compress and udder washing with proper hygine; Dry and keep udder clean with clean cloth and consistently wash your hands; clean bedding and attempt to neutralize temprature."
  }},
  {
  "Gangrenous Mastitis": {
    "keywords": ["Affected quarter is blue and cold to the touch", "Progressive discolouration from the tip to the top", "Necrotic parts drop off", "Cow often dies."],
    "diagnosis": "Likely Gangrenous Mastitis",
    "treatment\";":"Milk out gently 3x/day; Mix 1 teaspoon turmeric powder in 1 cup of clean warm water and use as a teat dip after milking; warm compress and udder washing with proper hygine; Dry and keep udder clean with clean cloth and consistently wash your hands; clean bedding and attempt to neutralize temprature; if condition worsens take antibiotics per reccomendation"
  }}
] 
