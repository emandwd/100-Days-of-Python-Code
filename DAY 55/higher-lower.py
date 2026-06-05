# https://flask.palletsprojects.com/en/stable/quickstart/#routing
# https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules
from flask import Flask
import random
random = random.randint(0,9)
print(random)

app = Flask(__name__)
@app.route('/')
def homepage():
    return "<h1> Guess a number between 0 and 9 </h1>" \
"<img src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' />"

@app.route("/<int:number>")
def guess(number):
    if number < random:
        return "<h1 style = 'color:red'> Too low, try again! </h1>"
    elif number > random:
        return "<h1 style = 'color:purple'> Your number is too high </h1>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__ == '__main__':
    app.run(debug=True)