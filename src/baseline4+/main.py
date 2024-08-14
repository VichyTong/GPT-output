import openai
import os
import json
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

openai.api_key = os.environ['OPENAI_API_KEY']


def noun_to_verb(noun):
    lemmatizer = WordNetLemmatizer()
    verb = lemmatizer.lemmatize(noun, wordnet.VERB)
    print(noun, verb)
    return verb


def get_instruction(isa_set, protocol, alias):
    name = noun_to_verb(protocol["name"])
    pro = json.dumps(protocol)
    if name in alias:
        name = alias[name]
    name = name.capitalize()
    if name not in isa_set:
        print("name not in isa: " + name)
        return None

    isa = json.dumps(isa_set[name])

    i = 50
    while i > 0:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": "You are a helpful assistant. Here is a protocol and a instruction manual, please tell me the instruction of the protocol. Output in the instruction json form. If you are not sure, output \"None\"."},
                    {"role": "user",
                     "content": 'Protocol: {{"name": "PCR", "reagent1": "BAP sequence", "reagent2": "pXa-1 plasmid(Promega, Madison, WI)", "product": "BAP PCR product", "origin": "1) Cloning of BAP in pDisplay. The BAP sequence is cloned between the N-terminal epitope of hemagglutinin A \(HA), which is preceded by a signal sequence from the murine Ig kappa-chain V-J2-C, and the C-terminal PDGF receptor transmembrane \(TM) domain generating the pBAP-TM plasmid encoding the HA-BAP-TM protein \(BAP-TM reporter)<sup>1</sup>.\r"}}\n Instruction : {"Incubate": {"required": ["reagent/sample", "temperature", "time"], "optional": ["equipment/notice"]}}'},
                    {"role": "assistant",
                     "content": '{"Incubate": "reagent/sample": ["BAP sequence", "pXa-1 plasmid"], "temperature": "None", "time": "None", "equipment/notice": "None"}'},
                    {"role": "user", "content": "Protocol: " + pro + "\nInstruction: " + isa}
                ],
                max_tokens=2000,
                temperature=0,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["END"]
            )
            break
        except:
            i -= 1


    resp = response['choices'][0]['message']['content']
    return resp


def main():
    with open("../../output/auto/prefer.json") as file:
        isa = json.load(file)
    with open("../../input/alias.json") as file:
        alias = json.load(file)
    with open("../../output/baseline4/output_protocol_nprot-4.json") as file:
        protocols = json.load(file)
    with open("../../output/baseline4+/output_protocol_nprot-4.json", "r") as file:
        now = json.load(file)
    for protocol in now:
        if "instruction" in protocol:
            print("already have instruction", protocol["name"])
            continue
        result = get_instruction(isa, protocol, alias)
        protocol["instruction"] = result
        with open("../../output/baseline4+/output_protocol_nprot-4.json", "w") as file:
            json.dump(now, file, indent=4)



main()
