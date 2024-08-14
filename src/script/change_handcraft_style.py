import json

with open('../../hand_crafted_ISA/isa.json', "r") as f:
    isa = json.load(f)


with open('../../hand_crafted_ISA/isa.json', 'w') as f:
    f.write(json.dumps(isa, indent=4))
