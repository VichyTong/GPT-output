import os
import json

from tqdm import tqdm

import utils


def reasoning(passage, sentence, phrase, model='gpt-3.5-turbo'):
    request = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": 'Please determine what does ' + phrase + ' refer to in the sentence provided by users in the following passages? If there is no text, please output None. Passage: ' + passage
            },
            {
                "role": "user",
                "content": "Sentence: " + sentence
            }
        ],
        "max_tokens": 1000,
        "temperature": 0,
        "top_p": 1,
    }

    resp = utils.request_openai(request)
    return resp


def main():
    directory = './input/selected_protocols/'
    protocol_dir = './input/separated_protocols/'
    k = 10
    for filename in tqdm(os.listdir(directory)):
        data = json.load(open(directory + filename, 'r'))
        passage = json.load(open(protocol_dir + filename, 'r'))
        output = []
        for item in data:
            refer = reasoning('\n'.join(passage[max(0, item["index"] - k): item["index"]]), item['string'],
                              item['phrase'])
            output.append({"index": item["index"], "string": item['string'], "phrase": item['phrase'], "refer": refer})
            with open('./input/refer_protocols/' + filename, 'w') as f:
                json.dump(output, f, indent=4)


if __name__ == '__main__':
    main()
