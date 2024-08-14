import json
import re

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def calculate_token_length(text):
    tokens = text.split(' ')
    token_length = 0

    for token in tokens:
        token_length += len(token)

    return token_length


def generate_templates(opcode, sentences, slots):
    prompt = f"You are a helpful assistant. Based on the following sentences related to the opcode '" + opcode + "' . Please decide which of these parameters are required and which are optional. Optional parameters will not appear in all sentences, mandatory parameters must appear in all sentences.\n"

    s = ""
    s += "Incubated 5 min at 25ºC, 60 min at 42ºC and 5 min at 72ºC with Improm-II® Reverse Transcriptase and Recombinant RNasin® \\(Promega) following the manufacturer instructions\n"
    s += "Incubated the mixture at room temperature for 15 min with gentle rotation.\n"
    s += "Incubated in cold PLP fix for 1 hour shaking at room temp.\n"
    s += "Incubated the membrane with secondary antibodies diluted in 5% fat-free dried milk in PBST \\(see Materials, Reagents for dilutions) for 45 to 60 min at room temperature with gentle agitation on a rocking plate.\n"

    k = r'parameter: "reagent/sample", "temperature", "time", "conditions"'

    t = ""

    slot_string = ", ".join(slots)
    print(slot_string)
    for sentence in sentences:
        t += sentence + '\n'
        tokens = t.split()
        token_length = len(tokens)
        if token_length > 1000:
            break
    print(t)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": s},
            {"role": "user", "content": k},
            {"role": "assistant", "content": '{"required" : ["reagent/sample", "temperature", "time"], "optional": ["conditions"]}'},

            {"role": "user", "content": t},
            {"role": "user", "content": "parameter: " + slot_string}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.1,
    )

    templates = response['choices'][0]['message']['content']
    print(templates)
    dictionary = json.loads(templates)
    print(dictionary)
    return dictionary


def main():
    collected_sentences_file = '../../input/cands_prefix.json'
    templates = read_json_file(collected_sentences_file)

    slots_file = '../../output/auto/slot.json'
    slots = read_json_file(slots_file)

    for key in templates.keys():
        matches = re.findall(r'\[(.*?)\]', key)
        word = matches[2]
        num = matches[1]
        if int(num) < 5:
            break
        if word not in slots:
            continue
        if not slots[word]["slot"]:
            continue

        with open('../../output/auto/prefer.json', 'r') as f:
            out = json.loads(f.read())
            if word in out:
                continue

        print(slots[word]["slot"])
        out[word] = generate_templates(word, templates[key], slots[word]["slot"])
        with open('../../output/auto/prefer.json', 'w') as outfile:
            json.dump(out, outfile, indent=4)


if __name__ == '__main__':
    main()
