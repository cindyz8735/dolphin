from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<file>')
def display_poem(file):
    with open(f'{file}.txt', 'r') as f:
        full_text = f.read()

    sources = []

    components = full_text.split('NEW\nNEW\n')

    for component in components:
        text = component.split('\n', 2)
        source = {'title': text[0],
                  'poem_title': text[1],
                  'stanzas': process_text(text[2])}
        sources.append(source)

    return render_template('poem.html', sources=sources, page_name=sources[0]['poem_title'])


def process_text(text):
    stanzas = text.split('\n\n')
    currently_italics = False
    diff_flag = 0

    res = []

    for i, stanza in enumerate(stanzas):
        lines = stanza.split('\n')
        res.append([])

        for j, line in enumerate(lines):
            words = line.split()
            res[i].append([])

            for word in words:
                if word == '<begin_i>':
                    currently_italics = True
                elif word == '<end_i>':
                    currently_italics = False
                elif word.startswith('<begin_diff_'):
                    diff_flag = word[-2]
                elif word == '<end_diff>':
                    diff_flag = 0
                else:
                    res[i][j].append((currently_italics, diff_flag, word))
    return res


if __name__ == '__main__':
    app.run(debug=True)

