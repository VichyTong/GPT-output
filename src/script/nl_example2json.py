import json
import re

with open("../../output/auto/labeled-isa.json", "r") as f:
    data = json.load(f)

results = {}

for key in data:
    detail = data[key]
    text_list = [key.title()]
    for syn in detail["synonym"]:
        text_list.append(syn.title())
    for text in text_list:
        results[text.upper()] = []
        for example in detail["example"]:
            if example.startswith("[" + text):
                results[text.upper()].append(example)


def parse_string(s):
    # Use a regular expression to find all [Word]{Word} patterns
    matches = re.findall(r'\[([^]]+)\]\{([^}]+)\}', s)

    # The result will be a list of tuples, each containing the bracketed word and the curly-brace word
    # Initialize the inner dictionary which will contain "emit" as a key
    inner_dict = {"emit": {}}

    # Process each match and populate the inner dictionary
    for item in matches:
        # The first element of the tuple is the word in brackets, the second is the word in braces
        inner_dict["emit"][item[1].lower()] = item[0]

    return inner_dict


for key in results:
    for text in results[key]:
        results[key][results[key].index(text)] = {
            "string": results[key][results[key].index(text)],
            "emit": parse_string(results[key][results[key].index(text)])["emit"]
        }


with open("../../output/auto/example.json", "w") as f:
    json.dump(results, f, indent=4)
