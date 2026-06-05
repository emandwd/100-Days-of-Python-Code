#https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules
#https://flask.palletsprojects.com/en/stable/quickstart/#routing
#https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask

app = Flask(__name__)
# To make text bold --> <b></b>
# To underline text --> <u></u>
# To make text bold AND underlined --> <b><u></u></b>
def make_bold(func):

@app.route("/") # Decorator
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
            '<p>This is a paragraph.</p> ' \
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2NpM2Uwa2d4bjJ1b3F4d283c3Z4emlkcDAzNzRsdmowdWxubmk0YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4VglqgTazN7YQ/giphy.gif">'

@app.route("/bye") # Decorator
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "<p>Bye, World!</p>"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
        return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
# in order to turn on the debug mode --> app.run(debug=True)
