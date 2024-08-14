import pandas as pd
import json

# 1. Load the JSON data
with open("./output/auto/human-modified-isa.json", "r") as file:
    data = json.load(file)

# 2. Flatten the data
flattened_data = []

for instruction, details in data.items():
    # This will keep track of maximum rows needed per instruction
    # based on the max count of items among slot, emit, notice, and synonym
    max_rows = max(len(details.get("slot", {})),
                   len(details.get("emit", {})),
                   len(details.get("notice", [])),
                   len(details.get("synonym", [])))

    for index in range(max_rows):
        row = {}
        row["Instruction"] = instruction if index == 0 else ""  # Fill instruction name only for the first row

        # Slot and Emit
        for category in ["slot", "emit"]:
            items = list(details.get(category, {}).items())
            if index < len(items):
                item, item_details = items[index]
                row[f"{category}_Item"] = item
                row[f"{category}_Required"] = item_details.get("require", "")
                row[f"{category}_Type"] = item_details.get("type", "")
                row[f"{category}_Comment"] = item_details.get("comment", "")
            else:
                row[f"{category}_Item"] = ""
                row[f"{category}_Required"] = ""
                row[f"{category}_Type"] = ""
                row[f"{category}_Comment"] = ""

        # Notice and Synonym
        for category in ["notice", "synonym", "example", "execution time", "correctness",
                         "violation of biology knowledge", "correction of biology knowledge"]:
            items = details.get(category, [])
            row[category] = items[index] if index < len(items) else ""

        flattened_data.append(row)

# 3. Convert flattened data to DataFrame
df = pd.DataFrame(flattened_data)

# 4. Write the DataFrame to Excel
df.to_excel("./output/auto/human-modified-isa.xlsx", index=False, engine="openpyxl")
