import json
import re

with open('../../input/cands_prefix.json') as f:
    data = json.load(f)

new_data = {}

for key in data:
    match = re.findall(r'\[(.*?)\]', key)
    if int(match[1]) < 12:
        continue
    if len(match[-1]) < 3:
        continue
    new_data[match[-1].upper()] = data[key]

with open('../../input/prefix.json', 'w') as f:
    json.dump(new_data, f, indent=4)