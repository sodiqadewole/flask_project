from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def home():  # put application's code here
#     return "Welcome to my website!";
#
# @app.route('/<name1>')
# def greetings(name1):
#     return "Welcome to the "+name1+"!"
#
# @app.route('/square/<int:number>')
# def show_square(number):
#     return "Square of " + str(number) + " is " + str(number * number)

@app.route("/")
def homepage():
    return "Paws Rescue Center 🐾"

@app.route('/about')
def about():
    return "We are a non-profit organization working as an animal rescue. " \
           "We aim to help you connect with the purrfect furbaby for you! " \
           "The animals you find on our website are rescued and rehabilitated animals. " \
           "Our mission is to promote the ideology 'adopt, don\'t hop'! "

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)