import os
import json

language_list = [
    "./output/auto/gpt-4-isa.json",
    "./output/auto/human-modified-isa.json",
    "./output/auto/labeled-isa.json",
]

data_list = []
for file_path in language_list:
    with open(file_path, "r") as f:
        data_list.append(json.load(f))

total_argument_cnt = 0

for verb in data_list[2]:
    for slot in data_list[2][verb]["slot"]:
        total_argument_cnt += 1
    for emit in data_list[2][verb]["emit"]:
        total_argument_cnt += 1

rate_list_0 = []
for verb in data_list[0]:
    if verb not in data_list[2]:
        rate_list_0.append(0)
        continue
    cnt = 0
    for slot in data_list[0][verb]["slot"]:
        if slot not in data_list[2][verb]["slot"]:
            continue
        if data_list[0][verb]["slot"][slot]["require"] != data_list[2][verb]["slot"][slot]["require"]:
            continue
        if data_list[0][verb]["slot"][slot]["type"] != data_list[2][verb]["slot"][slot]["type"]:
            continue
        cnt += 1
    for emit in data_list[0][verb]["emit"]:
        if emit not in data_list[2][verb]["emit"]:
            continue
        if data_list[0][verb]["emit"][emit]["require"] != data_list[2][verb]["emit"][emit]["require"]:
            continue
        if data_list[0][verb]["emit"][emit]["type"] != data_list[2][verb]["emit"][emit]["type"]:
            continue
        cnt += 1
    rate_list_0.append(cnt / (len(data_list[2][verb]["slot"]) + len(data_list[2][verb]["emit"])))

rate_list_1 = []
for verb in data_list[1]:
    if verb not in data_list[2]:
        rate_list_1.append(0)
        continue
    cnt = 0
    for slot in data_list[1][verb]["slot"]:
        if slot not in data_list[2][verb]["slot"]:
            continue
        if data_list[1][verb]["slot"][slot]["require"] != data_list[2][verb]["slot"][slot]["require"]:
            continue
        if data_list[1][verb]["slot"][slot]["type"] != data_list[2][verb]["slot"][slot]["type"]:
            continue
        cnt += 1
    for emit in data_list[1][verb]["emit"]:
        if emit not in data_list[2][verb]["emit"]:
            continue
        if data_list[1][verb]["emit"][emit]["require"] != data_list[2][verb]["emit"][emit]["require"]:
            continue
        if data_list[1][verb]["emit"][emit]["type"] != data_list[2][verb]["emit"][emit]["type"]:
            continue
        cnt += 1
    rate_list_1.append(cnt / (len(data_list[2][verb]["slot"]) + len(data_list[2][verb]["emit"])))

print(rate_list_1)

import matplotlib.pyplot as plt

# Box plot data
data = [rate_list_0, rate_list_1]
labels = ['GPT-only', 'GPT+non-expert']

# Create box plot
plt.boxplot(data, labels=labels)

# Add title and y-label
plt.title('Box Plot for Coverage Rate')
plt.ylabel('Rate')

# Show plot
plt.savefig("./output/figure/coverage_rate_and_informativeness.png")
