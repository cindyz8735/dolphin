from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<file>')
def display_poem(file):
    try:
        with open(f'static/texts/{file}.txt', 'r') as f:
            full_text = f.read()
    except OSError:
        return render_template('index.html')

    sources = []
    num_diffs = 0

    components = full_text.split('NEW\nNEW\n')

    for component in components:
        text = component.split('\n', 2)
        stanzas, diff = process_text(text[2])
        source = {'title': text[0],
                  'poem_title': text[1],
                  'stanzas': stanzas}
        sources.append(source)
        num_diffs = max(num_diffs, diff)

    return render_template('poem.html', sources=sources, page_name=sources[0]['poem_title'], num_diffs=num_diffs)


def process_text(text):
    stanzas = text.split('\n\n')
    currently_italics = False
    diff_flag = 0
    num_diff_flags = 0

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
                    num_diff_flags = max(num_diff_flags, int(diff_flag))
                elif word == '<end_diff>':
                    diff_flag = 0
                else:
                    res[i][j].append((currently_italics, diff_flag, word))
    return res, num_diff_flags


if __name__ == '__main__':
    app.run(debug=True)

