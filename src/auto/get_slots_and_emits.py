import json

# 读取输入文件
with open("../../output/auto/cluster.json", "r") as f:
    data = json.load(f)

# 创建一个新字典，用于存储参数列表
slots = {}

# 遍历每个操作步骤
for operation, description in data.items():
    # 将操作步骤描述分割成单词
    words = description.split()
    # 创建一个字典，用于存储参数和原始句子
    op_dict = {}
    # 创建一个列表，用于存储参数
    params = []
    # 遍历每个单词
    for word in words:
        # 如果单词包含尖括号，则将其去除尖括号后添加到参数列表中
        if "<" in word and ">" in word:
            params.append(word.strip("<").strip(">").strip(">."))
    # 将参数列表添加到字典中
    op_dict["slot"] = params
    # 将原始句子添加到字典中
    op_dict["example"] = description
    # 将字典添加到新字典中
    slots[operation] = op_dict


# 将参数字典写入输出文件
with open("../../output/auto/slot.json", "w") as f:
    json.dump(slots, f, indent=4)
