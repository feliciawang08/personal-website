from flask import Flask, render_template, url_for
app = Flask(__name__)
app.debug = True

print(__name__)

@app.route('/<username>/<int:favorite_num>')
def hello_world(username=None, favorite_num=0):
    print(url_for('static', filename='favicon.ico'))
    return render_template('index.html', username = username, favorite_num = favorite_num)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about')
def about_blog():
    return 'ABOUT BLOG'