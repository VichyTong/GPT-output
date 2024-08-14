import json

with open("../../output/auto/gpt-4-isa.json") as file:
    isa = json.load(file)

for key in isa:
    if len(isa[key]["example"]) > 5:
        isa[key]["example"] = isa[key]["example"][:5]

with open("../../output/auto/gpt-4-isa.json", "w") as file:
    json.dump(isa, file, indent=4)