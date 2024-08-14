import json
import utils


def add_argument(isa, sentence):
    i = 0
    print(json.dumps(isa))
    while i < len(sentence):
        ref = "\n".join(sentence[i: min(i + 50, len(sentence))])
        message = [
            {"role": "system",
             "content": "Is the following instruction can fully match the user's examples? If not, please add more arguments. Ouput in json format. Please note that the example given by the user may contain content that is not the instruction, usually at the end of the sentence. The added argument must have a comment to show its effect. If there is no more arguments needed, output None. Output in json form. instruction: " + json.dumps(
                 isa)},
            {"role": "user", "content": "Example: " + ref},
        ]
        response = utils.openai_request(message)
        print(response)
        if response != "None":
            isa = json.loads(response)
        i += 50
    return isa


def main():
    with open('./hand_crafted_ISA/isa.json', "r") as f:
        isa = json.load(f)

    with open('./input/cleaned_prefix.json') as f:
        data = json.load(f)

    with open('./output/auto/isa.json') as f:
        new = json.load(f)

    for key in isa:
        if key in new:
            continue
        sentence = data[key]
        new[key] = add_argument(isa[key], sentence)
        with open('./output/auto/isa.json', 'w') as f:
            f.write(json.dumps(new, indent=4))


if __name__ == '__main__':
    main()
