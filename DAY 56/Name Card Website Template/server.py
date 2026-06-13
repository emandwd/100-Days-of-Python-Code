from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
# jinja2.exceptions.TemplateNotFound: index.html means server.py is not in the same folder as templates/
if __name__ == '__main__':
    app.run(debug=True)