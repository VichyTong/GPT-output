import json
import argparse
import utils
import logging


def get_op_list(protocol, op_string, model):
    logging.info(">>> [get_op]" + protocol)
    request = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content":
                    f"""\
You are a helpful assistant. 

Task:
Given a protocol and a list of instructions, determine which part of the protocol is meaning a instruction.

List:
{json.dumps(op_string)}

Work Steps:
1. Read the protocol carefully.
2. Analyse the main steps of the protocol.
3. From the instruction list, select appropriate instructions that align with the protocol.
4. Output a JSON list of the selected instructions and the seperated protocols. 

Notes:
1. Some sentences serve as notices for the previous sentences. Please use as fewer instructions as possible to describe the protocol.
2. Output the instructions in right order that a human can follow it.
e.g. You need to calculate the concentration of the solution before you can use it.
3. Make sure the words you choose are all in the list, do not change the form.
                """
            },
            {
                "role": "user",
                "content": """
Protocol:
Take 2 ml of the solution into a 3 ml syringe and put a 27-gauge needle to the syringe. Avoid any air bubbles in the syringe.
"""
            },
            {
                "role": "assistant",
                "content": """
[
    {
        "instruction":"TAKE",
        "sentence":"Take 2 ml of the solution into a 3 ml syringe",
        "notice":"Avoid any air bubbles in the syringe."
    },
    {
        "instruction":"PUT",
        "sentence":"put a 27-gauge needle to the syringe.",
        "notice":"Avoid any air bubbles in the syringe."
    }
]
                """
            },
            {
                "role": "user",
                "content": f"Protocol:\n{protocol}"
            }
        ],
        "max_tokens": 1000,
        "temperature": 0,
        "top_p": 1,
    }
    ans = utils.request_openai(request)
    ans = ans.replace("\\", "\\\\")
    logging.info(ans)
    return json.loads(ans)


def fill_result(protocol, blank_file, model):
    print(">>> [fill_result]" + protocol)
    print(">>> [fill_result]" + blank_file)
    request = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": """
You are a helpful assistant.
Task:
You will be given a protocol, an associated manual, and a list of arguments in JSON format.
Based on the instructions provided, please  
Manual explanation:
- type: Specifies the type of information needed, such as reagent, string, number, volume, time, device, etc.
- comment: Describes the slot.

Filling blanks step:
1. Read the protocol and the manual carefully.
2. Use the most fitting term from your own knowledge to fill the blanks in the manual.

Note:
1. all of the blanks must be filled.
                """
            },
            {
                "role": "user",
                "content":
                    """\
Protocol:
Wash twice.

File need to be filled:
{"reagent1":"<blank>","reagent2":"<blank>"}

"""
            },
            {
                "role": "assistant",
                "content":
                    """\
{"reagent1":"washed cells_0","reagent2":"PBS"}
"""
            },
            {
                "role": "user",
                "content":
                    f"""\
    Protocol:
    {protocol}

    File need to be filled:
    {blank_file}
                        """
            }
        ],
        "max_tokens": 1000,
        "temperature": 0.4,
        "top_p": 1,
    }
    ans = utils.request_openai(request)
    ans = ans.replace("\\", "\\\\")
    print(ans)
    return json.loads(ans)


def get_instruction(model, protocol, passage, manual, blank_file, example, full_sentence):
    input_passage = []
    for item in passage:
        input_passage.append(
            {
                "instruction": item["instruction"],
                "emit_name": item["emit_name"],
                "protocol": item["protocol"]
            }
        )

    message = [
            {
                "role": "system",
                "content":
                    """\
You are a helpful assistant.
Task:
You will receive a protocol and an associated manual in JSON format. 
Based on the instructions, fill in the blanks in the JSON manual using information from the protocol and its context.

Manual explanation:
- require: Indicates if the slot is required (1) or optional (0).
- type: Specifies the type of information needed, such as reagent, string, number, volume, time, device, etc.
- comment: Describes the slot.

Filling blanks step:
1. Read the protocol and the manual carefully.
2. Use the most fitting term from the protocol or its context to fill the blanks in the manual.
3. Required slots and emits (require = 1) must be filled. Only optional slots and emits can be left as "None".

Note:
1. The required slots and emits must be filled, if you can not find them in protocol and context, use your own knowledge to fill it.
2. Retain the prefix in the chosen term. For instance, use "1ml solution" instead of just "solution".
3. You need to specify the output in reagent0.
4. Consider the context first when filling the blanks, note the name may be different from the context.
"""
            },
            {
                "role": "user",
                "content":
                    """\
Protocol:
Wash twice.

Context:
[{"name": "washed cells_0", "description" : "{1)  Wash cells in PBS supplemented with 2% FCS and incubate with mAb on ice for 30 min.}"}]

Manual: 
{"RINSE":{"slot":{"reagent1":{"require":1,"type":"string","comment":"The object to be rinsed"},"reagent2":{"require":1,"type":"reagent","comment":"The material used to rinse the object,defult = water"},"repeat":{"require":0,"type":"number","comment":"Number of times the object should be rinsed, default=1"},"time":{"require":0,"type":"time","comment":""},"notice":{"require":0,"type":"string","comment":""}},"emit":{"reagent0":{"require":1,"type":"reagent","comment":"The object after rinsing"}}}}

Example sentence:
[Rinse]{operation} the [wafer]{reagent1} in [DI water]{reagent2} for [10 seconds]{time}.

File need to be filled:
{"RINSE":{"reagent1":"<blank>","reagent2":"<blank>","repeat":"<blank>","time":"<blank>","notice":"<blank>","reagent0":"<blank>"}}
"""
            },
            {
                "role": "assistant",
                "content":
                    """\
{"RINSE":{"reagent1":"washed cells_0","reagent2":"PBS","repeat":"2","time":"None","notice":"None","reagent0":"washed cells_0"}}
"""
            },
            {
                "role": "user",
                "content":
                    f"""\
Protocol:
{protocol}

Context:
{input_passage}

Manual: 
{manual}

Example sentence:
{example}

File need to be filled:
{blank_file}
                """
            }
        ]

    print(message)

    request = {
        "model": model,
        "messages": message,
        "max_tokens": 2000,
        "temperature": 0,
        "top_p": 1,
    }

    resp = utils.request_openai(request)
    resp = resp.replace("\\", "\\\\")
    logging.info(f">>> [get_instruction] GPT_response: {resp} ")
    resp = json.loads(resp)
    del_list = []
    for item in resp:
        if resp[item] == "None":
            del_list.append(
                item
            )
    for x in del_list:
        del resp[x]
    manual = json.loads(manual)
    key = list(manual.keys())[0]
    out = {
        key: {
            "emit": [],
            "slot": []
        }
    }

    for item in resp:
        if item in manual[key]["slot"]:
            out[key]["slot"].append({
                item: resp[item]
            })
        elif item in manual[key]["emit"]:
            out[key]["emit"].append({
                item: resp[item]
            })
        else:
            raise Exception("Unknown type")

    logging.info(out)
    return out


def get_instruction_valina(model, protocol, passage):
    request = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content":
                    """\
You are a helpful assistant.
Task:
You will receive a protocol and the context, please output the protocol in a JSON format.
"""
            },
            {
                "role": "user",
                "content":
                    """\
Protocol:
Wash twice.

Context:
Wash cells in PBS supplemented with 2% FCS and incubate with mAb on ice for 30 min.
"""
            },
            {
                "role": "assistant",
                "content":
                    """\
{"RINSE":{"reagent1": "washed cells_0", "reagent2": "PBS", "repeat": "2", "time": "None", "notice": "None", "reagent0": "washed cells_0"}}
"""
            },
            {
                "role": "user",
                "content":
                    f"""\
Protocol:
{protocol}

Context:
{passage}
                """
            }
        ],
        "max_tokens": 2000,
        "temperature": 0,
        "top_p": 1,
    }

    resp = utils.request_openai(request)
    resp = resp.replace("\\", "\\\\")
    logging.info(f">>> [get_instruction_valina] GPT_response: {resp} ")
    resp = json.loads(resp)
    return resp


def extract_emit(instruction):
    out = []
    key = list(instruction.keys())[0]
    for item in instruction[key]["emit"]:
        out.append(item)
    return out


def link_edges(passage, instruction, index, second_index):
    print(">>> [link_edges] passage " + str(passage))
    print(">>> [link_edges] instruction " + str(instruction))

    edges = []
    key = list(instruction.keys())[0]
    used = []
    for item in instruction[key]["slot"]:
        name = list(item.keys())[0]
        for i in range(len(passage)):
            if passage[i]["emit_name"] == item[name]:
                edges.append({
                    "from": {
                        "index": passage[i]["index"],
                        "second_index": passage[i]["second_index"]
                    },
                    "to": {
                        "index": index,
                        "second_index": second_index
                    }
                })
                used.append(i)
                break

    new_passage = []
    for item in passage:
        if passage.index(item) not in used:
            new_passage.append(item)
    return edges, new_passage


def compile_text(op_list, isa, protocol, isa_map, passage, model, index):
    logging.info(f">>> [compile_text] protocol: {protocol}")
    logging.info(f">>> [compile_text] passage: {passage}")
    if protocol.strip() == "":
        return "", [], []
    op_list = get_op_list(protocol, op_list, model)
    out = []
    edges = []
    for second_index, item in enumerate(op_list):
        op = item["instruction"]
        sentence = item["sentence"]
        if "notice" in item:
            sentence += "\nnotice:\n" + item["notice"]

        try:
            map_op = isa_map[op]
        except KeyError:
            out.append({
                "error": f">>> [compile_text] {op} not in isa_map, protocol: {protocol}, op_list: {op_list}"
            })
            continue

        manual = {op: isa[map_op]}
        if "example" in manual[op]:
            del manual[op]["example"]
        if "notice" in manual[op]:
            del manual[op]["notice"]
        if "synonym" in manual[op]:
            del manual[op]["synonym"]
        manual = json.dumps(manual)
        logging.info(f">>> [compile_text] manual: {manual}")

        blank_file = {}

        for slot in isa[map_op]["slot"]:
            blank_file[slot] = "<blank>"
        for emit in isa[map_op]["emit"]:
            blank_file[emit] = "<blank>"
        blank_file = json.dumps(blank_file)
        logging.info(f">>> [compile_text] blank_file: {blank_file}")

        with open("../../output/auto/few_shot_examples.json", "r") as f:
            examples = json.load(f)
        example = examples[map_op]

        instruction = get_instruction(model, sentence, passage, manual, blank_file, example, protocol)
        out.append(instruction)

        edges_i, passage = link_edges(passage, instruction, index, second_index)
        edges.extend(edges_i)

        for i in extract_emit(instruction):
            reagent_name = list(i.keys())[0]
            passage.append({
                "instruction": op,
                "emit_name": i[reagent_name],
                "protocol": sentence,
                "index": index,
                "second_index": second_index
            })

    return out, edges, passage


def compile_list(op_list, isa, protocol, isa_map, model, type):
    passage = []
    out = []
    edges = []
    index = 0
    if type == "DSL":
        for item in protocol:
            if item["type"] == "title":
                continue
            elif item["type"] == "string":
                out_i, edges_i, passage = compile_text(op_list, isa, item["content"], isa_map, passage, model, index)
                out.append({
                    "sentence": item["content"],
                    "result": out_i
                })
                edges.extend(edges_i)
                index += 1
        return out, edges, passage
    elif type == "LLM":
        k = 5
        for item in protocol:
            if item["type"] == "title":
                continue
            elif item["type"] == "string":
                resp = get_instruction_valina(model, item["content"], passage)
                out.append({
                    "sentence": item["content"],
                    "result": resp
                })
                index += 1
                passage.append({
                    "instruction": item["content"]
                })
                while len(passage) > k:
                    passage.pop(0)
        return out, edges, passage


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='gpt-4')
    parser.add_argument('--file', type=str, default='')
    parser.add_argument('--type', type=str, default='DSL')
    args = parser.parse_args()
    model = args.model
    file = args.file
    compile_type = args.type

    with open("../../output/auto/labeled-isa.json") as f:
        isa = json.load(f)

    isa_map = {}

    op_list = []
    for key in isa:
        isa_map[key] = key
        op_list.append(key)
        for instruction in isa[key]["synonym"]:
            op_list.append(instruction)
            isa_map[instruction] = key

    with open(file, 'r') as f:
        data = json.load(f)

    f_name = file.split('/')[-1]
    print(f">>> [main] f_name: {f_name}")
    try:
        with open(f'../../output/auto/{compile_type}/instructions/' + f_name, 'r') as f:
            out = json.load(f)
    except FileNotFoundError:
        with open(f'../../output/auto/{compile_type}/instructions/' + f_name, 'w') as f:
            json.dump([], f, indent=4)
            out = []
    if out:
        print(">>> [main] " + str(len(out)) + " instructions already generated.")
        return

    compiled_list, edges, _ = compile_list(op_list, isa, data, isa_map, model, compile_type)

    with open(f'../../output/auto/{compile_type}/instructions/' + f_name, 'w') as f:
        json.dump(out + compiled_list, f, indent=4, ensure_ascii=False)
    with open(f'../../output/auto/{compile_type}/edges/' + f_name, 'w') as f:
        json.dump(edges, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
