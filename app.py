from flask import Flask, render_template, request

app = Flask(__name__)

def count_words(text):
    words = text.split()
    return len(words)

def format_words(text, format_type):
    if format_type == 'upper':
        return text.upper()
    elif format_type == 'lower':
        return text.lower()
    elif format_type == 'title':
        return text.title()
    else:
        return text

@app.route('/', methods=['GET', 'POST'])
def home():
    word_count = 0
    formatted_text = ""

    if request.method == 'POST':
        input_text = request.form['text']
        word_count = count_words(input_text)

        format_type = request.form.get('format_type', 'none')
        formatted_text = format_words(input_text, format_type)

    return render_template('index.html', word_count=word_count, formatted_text=formatted_text)

if __name__ == '__main__':
    app.run()
