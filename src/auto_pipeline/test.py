import html
import json

def html_decoder(html_text):
    return html.unescape(html_text)

# Example usage
encoded_html = "The temperature is 37&#xB0;C and the symbol is &#x3bc;"
decoded_text = html_decoder(encoded_html)
with open("./now.json", "w") as f:
    json.dump({"text": decoded_text}, f, indent=4, ensure_ascii=False)
