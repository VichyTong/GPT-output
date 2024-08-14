import json
import os
from tqdm import tqdm


def flatten_list(data: list):
    out = []
    for item in data:
        if isinstance(item, str):
            out.append({
                "type": "string",
                "content": item
            })
        elif isinstance(item, dict):
            out.append({
                "type": "title",
                "content": item["title"]
            })
            if isinstance(item["body"], str):
                out.append({
                    "type": "string",
                    "content": item["body"]
                })
            elif isinstance(item["body"], list):
                out.extend(flatten_list(item["body"]))
            else:
                raise Exception("Unknown type")
        else:
            raise Exception("Unknown type")
    return out


def main():
    files = []
    for root, ds, fs in os.walk("../../input/list_separated_protocols/"):
        files.extend(fs)
    for f_name in tqdm(files):
        with open("../../input/list_separated_protocols/" + f_name, 'r') as f:
            data = json.load(f)
        flattened_data = flatten_list(data)
        with open("../../input/flatten_protocols/" + f_name, "w") as file:
            json.dump(flattened_data, file, indent=4)


main()
