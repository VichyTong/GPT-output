import json

import nltk
from nltk.corpus import wordnet

# 下载所需的NLTK数据
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def get_infinitive(verb):
    lemmatizer = nltk.WordNetLemmatizer()
    infinitive = lemmatizer.lemmatize(verb, pos='v')
    return infinitive

def to_present_tense(data):
    words = []
    freq = []
    for i in data:
        words.append(i["opcode"])
        freq.append(i["frequency"])

    present_tense_words = []
    tagged_words = nltk.pos_tag(words)

    output = {}
    i = 0
    for word, pos in tagged_words:
        if pos.startswith('VB'):  # 如果是动词
            present_tense_word = get_infinitive(word)
            present_tense_words.append(present_tense_word)
            if present_tense_word not in output:
                output[present_tense_word] = freq[i]
            else:
                output[present_tense_word] += freq[i]
        i += 1
    return output


with open("../../output/auto/opcode_freq.json", "r") as f:
    data = json.load(f)
    with open("../../output/auto/opcode_freq_present_tense.json", "w", encoding='utf8') as out:
        freq = to_present_tense(data)
        output = []
        for i in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            tmp = {"opcode": i[0], "frequency": i[1]}
            output.append(tmp)
        json.dump(output, out, indent=4)
