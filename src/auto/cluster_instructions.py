import json
import re

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_templates(opcode, sentences):
    prompt = f"You are a helpful assistant. Based on the following sentences related to the opcode '" + opcode + "' , please summarize a manual templates for using this opcode. Here are a few requirements: 1. The manual should include slot(input) argument and emit(output) argument\n2. The argument needs to have a name, which corresponds to the three attributes of require, type, and comment. If you cannot remove this argument, you need to set require = 1. The argument that needs to be remarked needs to be added with comment, and it can be left blank if it is not needed.\n3. In the manual, some statements should be selected as examples, and all arguments should be covered in the examples, and should be as less as possible.\n4. If there are some precautions to be added to the command, add a new notice column, do not add a slot called notice.\n5. You can choose argument type from these options: [reagent, number, bool, string, temperature, time, volume, concentration], because this is a instruction in biology, reagent is the most useful type, reagent should contain all attributes like the volume, etc. For require arguments, you should set a default value in comment. 6. You should just output 4 or 5 examples. 7. Be careful to the \", you should output \\\" instead of \".\n"

    s = "Incubated 5 min at 25ºC, 60 min at 42ºC and 5 min at 72ºC with Improm-II® Reverse Transcriptase and " \
        "Recombinant RNasin® \\(Promega) following the manufacturer instructions\n"
    s += "Incubated the mixture at room temperature for 15 min with gentle rotation.\n"
    s += "Incubated in cold PLP fix for 1 hour shaking at room temp.\n"
    s += "Incubated the membrane with secondary antibodies diluted in 5% fat-free dried milk in PBST \\(see " \
         "Materials, Reagents for dilutions) for 45 to 60 min at room temperature with gentle agitation on a rocking " \
         "plate.\n"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": s},
            {"role": "assistant",
             "content": '{"slot": {"reagent1": {"require": 1, "type": "reagent", "comment": "The reagent to be incubated"}, "reagent2": {"require": 0, "type": "List<reagent>", "comment": "Additional reagents added during incubation"}, "temperature": {"require": 1, "type": "temperature", "comment": "default=room temperature"}, "time": {"require": 0, "type": "time", "comment": ""}, "environment": {"require": 0, "type": "string", "comment": ""}, "device": {"require": 0, "type": "string", "comment": ""}, "thermoProgram": {"require": 0, "type": "string", "comment": "when device=thermocycler, this parameter should be changed to REQ"}, "notice": {"require": 0, "type": "string", "comment": ""}}, "emit": {"reagent0": {"require": 1, "type": "reagent", "comment": ""}}, "example": ["[Incubate]{operation} at [room temperature]{temperature} for [30min]{time} [in the dark]{environment}.", "[Incubate]{operation} the [washed RBC]{reagent1} with [equal volume of bacteria]{reagent2} at [room temperature]{temperature} [under steady rotation at 6 rpm]{notice}.", "[Incubate]{operation} the [cells]{reagent1} again for [3 more hours]{time} at [BOD incubator]{device}.", "[Incubate]{operation} the reaction in [thermocycler]{device}: [1 cycle at 95\u00b0C for 5 min, 40 cycles of 95\u00b0C for 1 min, 60\u00b0C for 30 s and 72\u00b0C for 15 s, 1 cycle 72\u00b0C for 5 min and hold at 8\u00b0C]{thermoProgram}."], "notice": [], "synonym": []}'},
            {"role": "user", "content": "\n".join(sentences)},
        ],
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.1,
    )

    templates = response['choices'][0]['message']['content']
    print(templates)
    with open('../../output/auto/gpt-4-isa.json') as f:
        isa = json.load(f)
    isa[opcode] = json.loads(templates)
    with open('../../output/auto/gpt-4-isa.json', 'w') as f:
        json.dump(isa, f, indent=4)
    return templates


def get_close_opcode(opcode, isa_list):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant, given an opcode, help to choose the most close instruction of \"" + opcode + "\" from the instruction list. Just output the closet opcode. If there is no similar opcode, output \"None\". Instruction list: [" + "\n".join(
                    isa_list) + "]"
            }
        ]
    )

    return response['choices'][0]['message']['content']


def check_close_opcode(sentences, instruction):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Please help me decide whether the following example is similar to the given instruction, which gives another opcode usage. Its name is not the same as the verb in the example, but may have a similar meaning. If the opcode in example and instruction are similar, output \"True\", otherwise output \"False\""
            },
            {
                "role": "user",
                "content": "Instruction:" + instruction + "\n" + "Example:" + "\n".join(sentences) + "\n"
            }
        ]
    )

    return response['choices'][0]['message']['content']


def create_example(instruction, sentences):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You should give me examples of the instruction. Some statements should be selected as examples, and all arguments should be covered in the examples, and should be as less as possible. Just output 4-5 examples. Output in a json list."
            },
            {
                "role": "system",
                "content": 'Example : ["[Incubate]{operation} at [room temperature]{temperature} for [30min]{time} [in the dark]{environment}.", "[Incubate]{operation} the [washed RBC]{reagent1} with [equal volume of bacteria]{reagent2} at [room temperature]{temperature} [under steady rotation at 6 rpm]{notice}.", "[Incubate]{operation} the [cells]{reagent1} again for [3 more hours]{time} at [BOD incubator]{device}.", "[Incubate]{operation} the reaction in [thermocycler]{device}: [1 cycle at 95\u00b0C for 5 min, 40 cycles of 95\u00b0C for 1 min, 60\u00b0C for 30 s and 72\u00b0C for 15 s, 1 cycle 72\u00b0C for 5 min and hold at 8\u00b0C]{thermoProgram}.'
            },
            {
                "role": "user",
                "content": "Instruction:" + instruction + "\n" + "Sentences:" + "\n".join(sentences) + "\n"
            }
        ]
    )

    return response['choices'][0]['message']['content'].replace("\\", "\\\\")


def need_generate(opcode, sentences):
    with open('../../output/auto/gpt-4-isa.json') as f:
        isa = json.load(f)
    isa_list = [key for key in isa]

    if opcode in isa:
        return False

    for i in isa:
        if opcode in isa[i]["synonym"]:
            return False

    close_opcode = get_close_opcode(opcode, isa_list)
    print(close_opcode)
    if close_opcode == "None" or close_opcode not in isa:
        return True
    result = check_close_opcode(sentences, str({close_opcode: isa[close_opcode]}))
    print(result)
    if result == "True":
        with open('../../output/auto/gpt-4-isa.json') as f:
            isa = json.load(f)
        isa[close_opcode]["synonym"].append(opcode)
        example = create_example(opcode, sentences)
        print(example)
        isa[close_opcode]["example"].extend(json.loads(example))
        with open('../../output/auto/gpt-4-isa.json', 'w') as f:
            json.dump(isa, f, indent=4)
        return False
    else:
        return True


def main():
    with open('../../input/cleaned_prefix.json') as f:
        data = json.load(f)

    with open('../../input/control_instruction.json', "r") as f:
        control = json.load(f)

    i = 0
    for key in data:
        i += 1
        if key in control:
            continue
        print(">>> " + str(i) + "/" + str(len(data)) + " " + key)
        if need_generate(key, data[key]):
            generate_templates(key, data[key])


if __name__ == '__main__':
    main()
