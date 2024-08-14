import os
import json

directory = "output/auto/DSL/instructions"

# List all files and directories in the specified directory
all_items = os.listdir(directory)

# Filter out directories, keep only files
files = [item for item in all_items if os.path.isfile(os.path.join(directory, item))]

answer = {}
for file in files:
    with open(os.path.join(directory, file), "r") as f:
        data = json.load(f)
    for item in data:
        for result in item["result"]:
            if "error" in result:
                error_word = result["error"].split(",")[0].split("] ")[1].split("not")[0]
                if error_word not in answer:
                    answer[error_word] = 1
                else:
                    answer[error_word] += 1

print(json.dumps(answer, indent=4, sort_keys=True))
