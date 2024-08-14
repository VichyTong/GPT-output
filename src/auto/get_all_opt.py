import json

with open('../../output/auto/type.json') as f:
    op = json.load(f)

output = []

for key in op:
    output.append(key)

with open('../../output/auto/op.json', "w") as f:
    json.dump(output, f, indent=4)
