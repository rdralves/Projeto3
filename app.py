from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    variavel = 'Acerte o Número Secreto'
    num = randint(10, 13)

    if request.method == 'POST':
        palpite = int(request.form.get('name'))

        if num == palpite:
            return '<h1>Você Ganhou</h1>'
        else:
            return '<h1>Você Errou</h>'

    return render_template('index.html', variavel=variavel)




if __name__ == "__main__":
    app.run(debug=True)