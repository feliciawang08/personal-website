from flask import Flask, render_template, url_for
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('<string:page_name>')
def page(page_name="/"):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')