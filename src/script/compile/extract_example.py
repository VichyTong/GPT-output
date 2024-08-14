import json
import re

with open("output/auto/isa_with_one_example.json", 'r') as f:
    data = json.load(f)


def extract_first_word(sentence):
    pattern = r'\[([^\]]+)\]'
    match = re.search(pattern, sentence)
    if match:
        return match.group(1).upper()
    else:
        return None


out = {}
for item in data:
    flag = False
    for exp in data[item]["example"]:
        if extract_first_word(exp) == item:
            out[item] = exp
            flag = True
        if not flag:
            print("No example for synonym:", item)
    for s in data[item]["synonym"]:
        flag = False
        for exp in data[item]["example"]:
            if extract_first_word(exp) == s:
                out[s] = exp
                flag = True
        if not flag:
            print("No example for synonym:", s)

with open("output/auto/few_shot_examples.json", 'w') as f:
    json.dump(out, f, indent=4)
