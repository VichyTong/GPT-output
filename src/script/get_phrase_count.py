import os
import json
import re


def search_phrases_in_json_files(directory):
    # 预定义一组短语，大小写不敏感
    phrases = [
        "as previously described",
        "as mentioned earlier", "as stated before", "as noted above",
        "as outlined previously", "as indicated earlier", "as detailed above",
        "as highlighted earlier", "as discussed before", "as aforementioned",
        "as cited above", "as explained earlier", "as touched upon previously",
        "as referenced earlier", "as has been noted", "as previously mentioned",
        "as i have mentioned before", "as delineated above", "as recounted earlier",
        "as previously outlined", "as formerly described", "as observed earlier",
        "as established previously", "as confirmed before", "as identified above",
        "as reiterated", "as pointed out earlier", "as clarified previously",
        "as declared earlier", "as we have seen", "as previously noted",
        "as we discussed", "as already mentioned", "as alluded to earlier",
        "as formerly noted", "as was previously stated", "as mentioned beforehand",
        "as remarked earlier", "as initially described", "as earlier indicated",
        "as summed up previously", "as formerly indicated", "as set forth above",
        "as emphasized before", "as priorly noted", "as earlier delineated",
        "as previously asserted", "as underscored earlier", "as pre-established",
        "as depicted above", "as previously established"
    ]

    # 为每个短语编译一个不区分大小写的正则表达式
    regexes = [re.compile(re.escape(phrase), re.IGNORECASE) for phrase in phrases]

    # 初始化匹配成功的次数计数器
    match_count = 0

    # 遍历指定目录下的文件
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # 只处理.json文件
        if filename.endswith(".json"):
            with open(filepath, 'r', encoding='utf-8') as file:
                try:
                    # 加载JSON文件内容
                    data = json.load(file)
                    output = []
                    # 检查每一个字符串
                    for i, string in enumerate(data):
                        for j, regex in enumerate(regexes):
                            if regex.search(string):
                                print(f'Matched phrase in file {filename}: "{string}"')
                                # 找到匹配的字符串时，增加计数器
                                output.append({"index": i, "string": string, "phrase": phrases[j]})
                                match_count += 1
                                break
                    if len(output) > 0:
                        with open('./input/selected_protocols/' + filename, 'w') as f:
                            json.dump(output, f, indent=4)

                except json.JSONDecodeError:
                    print(f"Failed to decode JSON in file {filename}")

    # 输出总的匹配成功次数
    print(f'Total number of matches: {match_count}')


# 指定要遍历的文件夹路径
directory_path = "./input/separated_protocols/"
search_phrases_in_json_files(directory_path)
