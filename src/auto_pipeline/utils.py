import os
import time

import openai

openai.api_key = os.environ['OPENAI_API_KEY']


def request_openai(request):
    response = None
    i = 10
    while i > 0:
        try:
            response = openai.ChatCompletion.create(
                model=request['model'],
                messages=request['messages'],
                max_tokens=request['max_tokens'],
                temperature=request['temperature'],
                top_p=request['top_p'],
            )
            break
        except Exception as e:
            print(e)
            i -= 1
        time.sleep(10)
    if response is None:
        return None
    return response['choices'][0]['message']['content']