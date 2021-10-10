from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return "Welcome to my website!";

@app.route('/<name1>')
def greetings(name):
    return "Welcome to the "+name+"!"

@app.route('/test')
def test():
    return "new_test!"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)