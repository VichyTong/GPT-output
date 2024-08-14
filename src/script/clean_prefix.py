import openai
import os
import json

openai.api_key = os.environ['OPENAI_API_KEY']


def openai_request(message, temperature=0, top_p=1, max_tokens=4000, stop=None):
    i = 10
    response = None
    while i > 0:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=message,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                stop=stop,
            )
            break
        except Exception as e:
            print(e)
            i -= 1
    return response['choices'][0]['message']['content']


with open('../../input/prefix.json') as f:
    data = json.load(f)

with open('../../hand_crafted_ISA/isa.json') as f:
    isa = json.load(f)

with open('../../input/cleaned_prefix.json') as f:
    new_data = json.load(f)

with open('../../input/control_instruction.json', "r") as f:
    control = json.load(f)

print(len(new_data))
print(len(data))

for ins in data:
    if ins in new_data:
        continue

    if ins in control:
        continue

    new_example = []
    k = 0
    print(">>> " + ins)
    while k < len(data[ins]):
        example = "\n".join(data[ins][k: min(k + 100, len(data[ins]))])
        message = [
            {"role": "system",
             "content": "You are a helpful assistant. Please help me extract the exactly part related to {op} "
                        "operation from these sentences. If there is a clause with another verb in the example, "
                        "delete it. Output in a json list.".format(op=ins)},
            {"role": "user",
             "content": "Remove the supernatant, suspend in 10ml of HBSS containing 5mM EDTA, and incubate at 37 "
                        "&#xB0;C for 5 min.\nRemove the supernatant and dry the pellets using vacuum centrifuge."},
            {"role": "assistant", "content": '["Remove the supernatant", "Remove the supernatant"]'},
            {"role": "user", "content": "Example: " + example},
        ]
        response = openai_request(message)
        print(response)
        try:
            new_example.extend(json.loads(response.replace("\\", "\\\\")))
        except Exception as e:
            print(e)
        new_data[ins] = new_example
        with open('../../input/cleaned_prefix.json', 'w') as f:
            json.dump(new_data, f, indent=4)
        break
