from flask import Flask, render_template, url_for
app=Flask(__name__)

posts=[{
    'author':'Jahongir Mingliboyev',
    'title':'How to get taller',
    'content':'Daily effort is required to get taller, and it is not easy',
    'date':'Feb 10, 2026'
},{'author':'Dilnoza Mingliboyeva',
    'title':'Reading books makes you smart',
    'content':'If you want to think differently, I recommend you to read a book 30 minutes daily',
    'date':'Feb 9, 2026'}
]

@app.route("/")
def hello_world():
    return render_template('main.html', posts=posts, title='Home Page')

@app.route("/about")
def about():
    return render_template('about.html', title="About Page")

if __name__ == "__main__":
    app.run(debug=True)
