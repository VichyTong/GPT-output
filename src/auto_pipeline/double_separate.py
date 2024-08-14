import json
import os

from tqdm import tqdm


def separate(directory, name, isa_list):
    with open(directory + name, 'r') as f:
        data = json.load(f)
    res = []
    for s in data:
        now = [s]
        ans = []
        while len(now) > 0:
            x = now[-1]
            x = now.pop()
            flag = False
            for isa in isa_list:
                if isa in x:
                    sep = x.split(isa)
                    sep[1] = isa.capitalize() + sep[1]
                    now.append(sep[1])
                    now.append(sep[0])
                    flag = True
                    break
            if not flag:
                ans.append(x)
        res.extend(ans)

    return res


def main():
    with open("../../output/auto/human-modified-isa.json") as file:
        isa = json.load(file)

    isa_list = []

    for key in isa:
        isa_list.append(key.lower() + ' ')
        for instruction in isa[key]["synonym"]:
            isa_list.append(instruction.lower() + ' ')

    files = []
    for root, ds, fs in os.walk("../../input/separated_protocols/"):
        files.extend(fs)
    for f_name in tqdm(files):
        protocols = separate('../../input/separated_protocols/', f_name, isa_list)
        with open("../../input/double_separated_protocols/" + f_name, "w") as file:
            json.dump(protocols, file, indent=4)


if __name__ == '__main__':
    main()
