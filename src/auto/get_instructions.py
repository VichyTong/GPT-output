import json
import os
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_top_opcodes(data, top_n=100):
    stop_set = {
        "be": True,
        "do": True,
        "make": True,
        "say": True,
        "get": True,
        "go": True,
        "know": True,
        "take": True,
        'use': True,
        "follow": True,
        "collect": True,
        "describe": True,
    }
    new_data = []
    for item in data:
        if item['opcode'] not in stop_set:
            new_data.append(item)
    sorted_data = sorted(new_data, key=lambda x: x['frequency'], reverse=True)
    top_opcodes = [item['opcode'] for item in sorted_data[:top_n]]
    return top_opcodes


def lemmatize_opcodes(data):
    lemmatizer = WordNetLemmatizer()
    lemmatized_data = {}

    for opcode, value in data.items():
        present_tense_opcode = lemmatizer.lemmatize(opcode, pos='v')
        lemmatized_data[present_tense_opcode] = value

    return lemmatized_data


def collect_sentences(top_opcodes, folder_path):
    collected_sentences = {}

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.jsonl'):
            file_path = os.path.join(folder_path, file_name)
            data = read_json_file(file_path)
            lemmatized_data = lemmatize_opcodes(data)

            for opcode in top_opcodes:
                if opcode in lemmatized_data:
                    if opcode not in collected_sentences:
                        collected_sentences[opcode] = set()

                    collected_sentences[opcode].update(lemmatized_data[opcode]['Sentences'])

    # 将 set 转换为 list
    for opcode in collected_sentences:
        collected_sentences[opcode] = list(collected_sentences[opcode])

    return collected_sentences


def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    top_opcodes_file = '../../output/auto/opcode_freq_present_tense.json'
    protocol_folder = '../../output/auto/protocol'
    output_file = '../../output/auto/collected_sentences.json'

    top_opcodes_data = read_json_file(top_opcodes_file)
    top_opcodes = get_top_opcodes(top_opcodes_data)

    for x in top_opcodes:
        print(x)

    collected_sentences = collect_sentences(top_opcodes, protocol_folder)
    save_to_json(collected_sentences, output_file)


if __name__ == '__main__':
    main()
