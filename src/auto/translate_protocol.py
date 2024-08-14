import sys
import re
import openai
import os
import json

openai.api_key = os.environ['OPENAI_API_KEY']


def get_op(protocol, op_string):
    print(protocol)
    i = 10
    while i > 0:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system",
                     "content": "You are a helpful assistant. Here is a protocol and a instruction manual, please tell me what operation is mentioned in the protocol. Output in the operation in json form. If you are not sure, output \"None\". You can just output the operation form the manual. Just output a json list, output the instruction only once."},
                    {"role": "system",
                     "content": "manual: " + op_string},
                    {"role": "user",
                     "content": "1) Cloning of BAP in pDisplay. The BAP sequence is cloned between the N-terminal epitope of hemagglutinin A \(HA), which is preceded by a signal sequence from the murine Ig kappa-chain V-J2-C, and the C-terminal PDGF receptor transmembrane \(TM) domain generating the pBAP-TM plasmid encoding the HA-BAP-TM protein \(BAP-TM reporter)<sup>1</sup>."},
                    {"role": "assistant",
                     "content": '["incubate", "add"]'},
                    {"role": "user", "content": protocol}
                ],
                max_tokens=100,
                temperature=0.1,
                top_p=1,
            )
            break
        except Exception as e:
            print(e)
            i -= 1
    resp = response['choices'][0]['message']['content']
    print(resp)
    out = []
    matches = re.findall(r'"([^"]+)"', resp)
    if matches is None:
        return None
    for match in matches:
        out.append(match)
    if out is None:
        return None
    return out


def get_instruction(op_string, isa, protocol):
    out = []
    op = get_op(protocol, op_string)

    if op is None:
        return

    for o in op:
        i = 10
        o = o.upper()
        if o not in isa:
            print('>>> operation ' + o + " is not in ISA.")
            continue
        manual = str(isa[o])
        print(manual)
        while i > 0:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant. Here is a protocol and a instruction manual, please tell me the instruction of the protocol. Output in the instruction json form. If you are not sure, output \"None\"."
                        },
                        {
                            "role": "user",
                            "content": 'protocol : 1) Cloning of BAP in pDisplay. The BAP sequence is cloned between the N-terminal epitope of hemagglutinin A \(HA), which is preceded by a signal sequence from the murine Ig kappa-chain V-J2-C, and the C-terminal PDGF receptor transmembrane \(TM) domain generating the pBAP-TM plasmid encoding the HA-BAP-TM protein \(BAP-TM reporter)<sup>1</sup>'
                        },
                        {
                            "role": "user",
                            "content": 'manual : "INCUBATE": {"emit": {"r0": "REG"},"example": "incubate {reagent/sample} at {temperature} for {time} with {equipment/notice}","slot": {"equipment": {"comment": "","require": 0,"type": "STR"},"reagent": {"comment": "","require": 1,"type": "STR"},"sample": {"comment": "","require": 1,"type": "STR"},"temperature": {"comment": "","require": 1,"type": "TEMP"},"time": {"comment": "","require": 1,"type": "TIME"}}},'
                        },
                        {
                            "role": "assistant",
                            "content": '{"INCUBATE": {"emit": {"r0": "BAP"}, "slot":{"reagent": ["hemagglutinin A", "pXa-1 plasmid, murine Ig kappa-chain V-J2-C"], "sample": [""], "temperature": [""], "time": [""]}}}'
                        },
                        {
                            "role": "user",
                            "content": "protocol: " + protocol
                        },
                        {
                            "role": "user",
                            "content": "manual" + manual
                        }
                    ],
                    max_tokens=2000,
                    temperature=0.1,
                    top_p=1,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                    stop=None,
                )
                break
            except Exception as e:
                print(e)
                i -= 1

        resp = response['choices'][0]['message']['content']
        if resp == "None":
            return None
        print(">>>GPT " + resp)
        out.append({o: json.loads(resp)})
    return out


def is_meaningful(s):
    if len(s) < 10:
        return False
    else:
        return True


def parse_file(path, filename):
    res = []
    with open(path + filename, 'r') as f:
        data = json.load(f)
        procedure_text = ""
        for text in data["content"]:
            if text["header"] == "Procedure":
                procedure_text = text["content"]
        procedure_divided = procedure_text.replace('\n', '').split('. ')
        for procedure in procedure_divided:
            if is_meaningful(procedure):
                res.append(procedure)
    return res


def main():
    f_name = sys.argv[1]
    print("../../protocols/" + f_name)
    protocols = parse_file('../../protocols/', f_name)

    with open("../../output/auto/new_instruction.json") as file:
        isa = json.load(file)
    with open("../../output/auto/op.json") as file:
        op = json.load(file)
    op_string = ", ".join(op)

    try:
        with open("../../output/auto/instructions/output_protocol_" + f_name, "r") as file:
            now = json.load(file)
    except FileNotFoundError:
        with open("../../output/auto/instructions/output_protocol_" + f_name, "w") as file:
            json.dump({}, file, indent=4)
            now = {}

    for protocol in protocols:
        if protocol not in now:
            tmp = get_instruction(op_string, isa, protocol)
            if tmp is None:
                now[protocol] = []
            else:
                now[protocol] = tmp
            with open("../../output/auto/instructions/output_protocol_" + f_name, "w") as file:
                json.dump(now, file, indent=4)


main()
