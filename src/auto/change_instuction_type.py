import json
import openai
import os


# def generate_emit(instruction):
#     openai.api_key = os.getenv("OPENAI_API_KEY")
#     prompt = "You are a helpful assistant. Please help to decide the emits of the following instruction. Output in a json format. For the example, the output is reagent because add instruction returns a new reagent."
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": prompt},
#             {"role": "user",
#              "content": '"Add": {"required": {"reagent": "STR","solution": "STR","action": "STR"},"optional": {"time": "TIME","temperature": "TEMP","equipment": "STR","notice": "STR"'},
#             {"role": "assistant", "content": '[{"reagent": "STR"}]'},
#             {"role": "user", "content": instruction},
#         ],
#         max_tokens=1000,
#         n=1,
#         stop=None,
#         temperature=0,
#     )
#     result = response['choices'][0]['message']['content']
#     return json.loads(result)
#


def get_example(key):
    with open('output/auto/slot.json') as f:
        data = json.load(f)
    return data[key]["example"].replace("<", "{").replace(">", "}")


def main():
    with open('output/auto/type.json') as f:
        data = json.load(f)

    output = {}

    for key in data:
        slot = {}
        for i in data[key]["required"]:
            slot[i] = {
                "require": 1,
                "type": data[key]["required"][i],
                "comment": ""
            }
        if "optional" in data[key]:
            for i in data[key]["optional"]:
                slot[i] = {
                    "require": 0,
                    "type": data[key]["optional"][i],
                    "comment": ""
                }
        output[key.upper()] = {
            "slot": slot,
            "emit": {"r0": {"comment": "", "require": 1, "type": "REG"}},
            "example": get_example(key)
        }

    with open('output/auto/new_instruction.json', 'w') as f:
        json.dump(output, f, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()
