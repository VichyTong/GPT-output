import json

with open('../../output/auto/human-modified-isa.json', 'r') as f:
    isa = json.load(f)

output = []
for index, key in enumerate(isa):
    output.append("## " + str(index + 1) + ". " + key)

    examples = isa[key]['example']
    output.append("\n### Examples:")
    for example in examples:
        output.append("- " + example)

    notices = isa[key]['notice']
    output.append("\n### Notices:")
    for notice in notices:
        output.append("- " + notice)

    synonyms = isa[key]['synonym']
    output.append("\n### Synonyms:")
    for synonym in synonyms:
        output.append("- " + synonym)

    output.append("\nArguments:")
    output.append("\n| Argument | Type | Comment |")
    output.append("| --- | --- | --- |")
    slot = isa[key]['slot']
    for arg in isa[key]['slot']:
        output.append("| " + arg + " | " + ("required" if slot[arg]['require'] else "optional") + " \| " + slot[arg]['type'] + " | " + slot[arg]['comment'] + " |")
    emit = isa[key]['emit']
    for arg in isa[key]['emit']:
        output.append("| " + arg + " | " + ("required" if emit[arg]['require'] else "optional") + " \| " + emit[arg]['type'] + " | " + emit[arg]['comment'] + " |")

with open("../../output/auto/human-modified-isa.md", 'w') as f:
    f.write("\n".join(output))
