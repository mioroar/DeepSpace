from flask import Flask, request, render_template
import gameweb

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('command')
        game_output = gameweb.deepspace_battle(user_input)
    else:
        game_output = gameweb.deepspace_battle()  # Показать приветственное сообщение сразу
    return render_template('deepspace.html', output=game_output)


if __name__ == "__main__":
    app.run(debug=True)
