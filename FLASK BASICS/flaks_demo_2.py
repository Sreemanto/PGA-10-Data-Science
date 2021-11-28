from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>This is my home page<h1>"

@app.route('/about')
def about():
    return "This about us page. We are a tech company"


@app.route('/contactus')
def contactus():
    return "<h1>Office : 022-33114949</h1>"

if __name__ == '__main__':
    app.run(debug=True)
