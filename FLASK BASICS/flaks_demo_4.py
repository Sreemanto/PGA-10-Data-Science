from flask import Flask, render_template

app = Flask(__name__)

content = [

{
"Author" : "Sreemanto Kesh",
"title" : "Blog 1",
"content" : "Data Science",
"date" : "27th Nov"
},
{
"Author" : "Sreemanto Kesh",
"title" : "Blog 2",
"content" : "Machine Learning",
"date" : "28th Nov"
}

]


@app.route('/')
def home():
    return render_template("home2.html", posts = content)

@app.route('/about')
def about():
    return "<h1>This about us page. We are a tech company<h1>"


if __name__ == '__main__':
    app.run(debug=True)
