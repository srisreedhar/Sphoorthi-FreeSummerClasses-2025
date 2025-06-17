# importing the Flask Library
from flask import Flask

# create a Name space for our application
firstapp = Flask(__name__)

# @firstapp.route("/") - Router function
# Router Decorator - create URLs using this decorator
@firstapp.route("/hello")
def hello_world():
    return """ Hello All, Sphoorthi Oum, Welcome to the Session"""


# View Function
# we create a function for every page that we want to create
# def hello_world():
#     return "<p>Hello, World!</p>"

# helloworld() is the view function, a function for webpage whose address is /hello

@firstapp.route("/python")
def python():
    return """ python page """



if __name__ == '__main__':
	firstapp.run(debug=True)   