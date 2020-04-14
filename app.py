from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def process_texts():
    with open('1973_doubt_2.txt', 'r') as file:
        text = file.read()

    stanzas = text.split('\n\n')
    formatting = []
    currently_italics = False

    res = []

    for i, stanza in enumerate(stanzas):
        lines = stanza.split('\n')
        res.append([])

        for j, line in enumerate(lines):
            words = line.split()
            res[i].append([])

            for k, word in enumerate(words):
                if word == '<begin_i>':
                    currently_italics = True
                elif word == '<end_i>':
                    currently_italics = False

                else:
                    res[i][j].append((currently_italics, word))

    return render_template('poem.html', source_title='The Dolphin, 1973',
                           poem_title='Doubt 2: "Pointing the Horns of the Dilemma"', stanzas=res)


if __name__ == '__main__':
    app.run(debug=True)

