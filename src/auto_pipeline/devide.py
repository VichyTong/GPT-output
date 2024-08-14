import json
import os
from tqdm import tqdm
import spacy


def split_text(text: str):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [sent.text for sent in doc.sents]


def split_list(data: list):
    out = []
    for item in data:
        if isinstance(item, str):
            out += split_text(item)
        elif isinstance(item, dict):
            if isinstance(item["body"], str):
                item["body"] = split_text(item["body"])
            elif isinstance(item["body"], list):
                item["body"] = split_list(item["body"])
            else:
                raise Exception("Unknown type")
            out.append(item)
        else:
            raise Exception("Unknown type")
    return out


def parse_file(path, filename):
    with open(path + filename, 'r') as f:
        data = json.load(f)
        procedure_divided = split_list(data)
    return procedure_divided


def main():
    files = []
    for root, ds, fs in os.walk("../../input/list_separated_protocols/"):
        files.extend(fs)
    for f_name in tqdm(files):
        protocols = parse_file('../../input/list_separated_protocols/', f_name)
        with open("../../input/list_separated_protocols/" + f_name, "w") as file:
            json.dump(protocols, file, indent=4)


if __name__ == '__main__':
    main()
