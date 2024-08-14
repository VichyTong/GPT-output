import os
import json

files = []
for root, ds, fs in os.walk("output/auto/DSL/instructions"):
    files.extend(fs)

for item in files:
    if not item.startswith("protocol_nprot"):
        continue
    # if exist in ground truth
    name = item.split(".")[0].split("_")[1]
    if os.path.exists(f"output/ground_truth/{name}_graphData.json"):
        with open(f"output/ground_truth/{name}_graphData.json", 'r') as f:
            ground_truth = json.load(f)
    else:
        raise Exception("Ground truth not found")
    with open("output/auto/DSL/instructions/" + item, 'r') as f:
        data = json.load(f)

    ground_l = []
    for i in ground_truth["nodes"]:
        ground_l.append(i["text"])

    correct_num = 0
    print(name)
    for i in data:
        print(">>> i: " + i["sentence"])
    for j in ground_l:
        print(">>> j: " + j)

    print(correct_num / len(ground_l))
