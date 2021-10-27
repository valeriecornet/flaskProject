"""Flask project"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<temperature>')
def f(temperature=""):
    fahrenheit = float(temperature) * 9.0 / 5 + 32
    return "{}".format(fahrenheit)


if __name__ == '__main__':
    app.run()
