from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about/blog')
def about_blog():
    return 'Blog'