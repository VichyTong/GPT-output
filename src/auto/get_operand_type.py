import json

import openai
import os
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

openai.api_key = os.getenv("OPENAI_API_KEY")


def choose_type(op_list):
    tagged_sent = pos_tag(op_list)
    wnl = WordNetLemmatizer()
    lemmas_sent = []
    for tag in tagged_sent:
        wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
        lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos))

    out = {}
    with open('../../output/auto/cache.json', 'r') as f:
        cache = json.loads(f.read())
    for op in lemmas_sent:
        if op in cache:
            out[op] = cache[op]
        else:
            prompt = f"You are a helpful assistant. Please choose the type of the operand given from the user.\n There are 7 types of operands: STR for string, TIME for time, TEMP for temprature, CONC for concentration, VOL for volume, NUM for number, and BOOL\n If you are not sure about the type, output None\n"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": "reagent"},
                    {"role": "assistant", "content": "STR"},
                    {"role": "user", "content": "equipment"},
                    {"role": "assistant", "content": "STR"},
                    {"role": "user", "content": "time"},
                    {"role": "assistant", "content": "TIME"},
                    {"role": "user", "content": "duration"},
                    {"role": "assistant", "content": "TIME"},
                    {"role": "user", "content": op}
                ],
                max_tokens=1000,
                n=1,
                temperature=0,
            )
            res = response['choices'][0]['message']['content']
            if res.find("None") != -1:
                out[op] = "STR"
                cache[op] = "STR"
            else:
                cache[op] = res
                out[op] = res
            with open('../../output/auto/cache.json', 'w') as f:
                json.dump(cache, f, indent=4)
            print(op, res)
    return out


def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def generate_type(operand):
    op_list = []
    for op in operand:
        op = op.lower()
        if op.find("/"):
            tmp = op.split("/")
            for t in tmp:
                op_list.append(t)
        else:
            op_list.append(op)
    return choose_type(op_list)


def main():
    with open("../../output/auto/prefer.json") as f:
        data = json.load(f)
        output = data
        for opcode in data:
            required_operand = data[opcode]["required"]
            output[opcode]["required"] = generate_type(required_operand)
            if "optional" in data[opcode]:
                optional_operand = data[opcode]["optional"]
                output[opcode]["optional"] = generate_type(optional_operand)
            with open("../../output/auto/type.json", "w") as out:
                json.dump(output, out, indent=4)


if __name__ == '__main__':
    main()
