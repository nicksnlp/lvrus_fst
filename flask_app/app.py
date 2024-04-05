from flask import Flask, request, jsonify

app = Flask(__name__)

"""
# Sample translation function, replace it with your actual translation logic
def translate_word(word, lang):
    translations = {
        "latvian": {
            "hello": "sveiki",
            "world": "pasaule",
            # Add more Latvian translations as needed
        },
        "russian": {
            "hello": "привет",
            "world": "мир",
            # Add more Russian translations as needed
        }
    }
    return translations.get(lang, {}).get(word.lower(), "Translation not found")

@app.route('/translate', methods=['GET'])
def translate():
    word = request.args.get('word', '')
    lang = request.args.get('lang', 'latvian')  # Default to Latvian if language not specified
    translation = translate_word(word, lang)
    return jsonify({'translation': translation})

if __name__ == '__main__':
    app.run(debug=True)
"""
