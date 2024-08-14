import json
import os


# def get_arg(item: str):
#
#
#
# def get_list(data):
#     for item in data:
#         if isinstance(item, str):
#             get_arg(item)
#         elif isinstance(item, dict):
#             if isinstance(item["body"], str):
#                 get_arg(item["body"])
#             elif isinstance(item["body"], list):
#                 get_list(item["body"])
#             else:
#                 raise Exception("Unknown type")
#
#         else:
#             raise Exception("Unknown type")
#
# file_list = []
# for root, dirs, files in os.walk("../../output/auto/instructions"):
#     for file in files:
#         file_list.append(os.path.join(root, file))
#
# for file in file_list:
#     print(file)
#     with open(file, 'r') as f:
#         data = json.load(f)
#         get_list(data)

with open("../../output/auto/labeled-isa.json", 'r') as f:
    data = json.load(f)


item_list = []
for key in data:
    item = data[key]
    for i in item["slot"]:
        item_list.append({i: item["slot"][i]})
    for i in item["emit"]:
        item_list.append({i: item["emit"][i]})

info_dict = {}

for item in item_list:
    for key, info in item.items():
        if key in info_dict:
            info_dict[key].append(info)
        else:
            info_dict[key] = [info]

# Step 2: Filter keys with more than one entry
dup_info = {key: infos for key, infos in info_dict.items() if len(infos) > 1}

# Convert the dictionary to a list of the desired format
result = [{"key": key, "info": infos} for key, infos in dup_info.items()]

# Print or return the result as needed
sorted_list = sorted(result, key=lambda x: x["key"])
with open("../../output/auto/arguments.json", "w") as f:
    json.dump(sorted_list, f, indent=4)

keys_only = [d['key'] for d in sorted_list]
with open("../../output/auto/arguments_name.json", "w") as f:
    json.dump(keys_only, f, indent=4)
