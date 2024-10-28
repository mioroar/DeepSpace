from flask import Flask, render_template, request, redirect, url_for
import sys
import main
import os
app = Flask(__name__)


# Обработка главной страницы
@app.route('/')
def index():
    return render_template('index.html')


# Обработка страницы командного центра DeepSpace
@app.route('/deepspace', methods=['GET', 'POST'])
def deepspace():
    if request.method == 'POST':
        command = request.form.get('command')
        # Здесь можно обработать команду, например, записать в лог или выполнить какое-то действие
        response_text = f"Received command: {command}"  # Пример ответа
        return render_template('deepspace.html', text=response_text)
    else:
        return render_template('deepspace.html', text="")


if __name__ == '__main__':
    app.run(debug=True)
