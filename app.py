import random
from flask import Flask, render_template, request

app = Flask(__name__)

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"

def generate_password(nr_letters, nr_symbols, nr_numbers):
    password = "".join(random.choices(letters, k=nr_letters)) + \
               "".join(random.choices(symbols, k=nr_symbols)) + \
               "".join(random.choices(numbers, k=nr_numbers))
    return "".join(random.sample(password, len(password)))

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""
    if request.method == 'POST':
        nr_letters = int(request.form['letters'])
        nr_symbols = int(request.form['symbols'])
        nr_numbers = int(request.form['numbers'])
        password = generate_password(nr_letters, nr_symbols, nr_numbers)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
