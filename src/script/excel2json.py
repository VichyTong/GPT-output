import pandas as pd
import json
import math

# 1. Read the Excel file using pandas
df = pd.read_excel("./output/auto/labeled-human-modified-isa.xlsx", engine="openpyxl")

# 2. Reconstruct the JSON structure
data = {}
current_instruction = None

for _, row in df.iterrows():
    instruction = row["Instruction"] if pd.notna(row["Instruction"]) else current_instruction

    if instruction not in data:
        data[instruction] = {
            "slot": {},
            "emit": {},
            "notice": [],
            "synonym": [],
            "example": [],
            "execution time": []
        }

    # Handle slot and emit
    for category in ["slot", "emit"]:
        item = row[f"{category}_Item"]
        if pd.notna(item):
            data[instruction][category][item] = {
                "require": row[f"{category}_Required"],
                "type": row[f"{category}_Type"],
                "comment": row[f"{category}_Comment"]
            }

    for category in ["slot"]:
        item = row[f"{category}_Item"]
        if pd.notna(item):
            data[instruction][category][item]["correctness"] = row[f"correctness"]
            data[instruction][category][item]["violation of biology knowledge"] = row[f"violation of biology knowledge"]
            data[instruction][category][item]["correction of biology knowledge"] = row[f"correction of biology knowledge"]


    # Handle notice, synonym, and other categories
    for category in ["notice", "synonym", "example", "execution time"]:
        item = row[category]
        if pd.notna(item):
            data[instruction][category].append(item)

    current_instruction = instruction


def replace_nan(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, float) and math.isnan(value):
                obj[key] = ""
            else:
                replace_nan(value)
    elif isinstance(obj, list):
        for index, item in enumerate(obj):
            if isinstance(item, float) and math.isnan(item):
                obj[index] = ""
            else:
                replace_nan(item)
    return obj


data = replace_nan(data)

# 3. Write the JSON structure to a file
with open("./output/auto/reconstructed-labeled-human-modified-isa.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("JSON has been reconstructed and saved to 'reconstructed-human-modified-isa.json'")
