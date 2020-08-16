from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

# handles contact information form
@app.route('/form_submission_success', methods = ['GET', 'POST'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        write_data(data)
        return render_template('formsubmitted.html')
    else:
        return "form not submitted."

# Write contact information to database text file
def write_data(data):
    email = data['email']
    subject = data['subject']
    message = data["message"]
    with open('database.txt', 'a') as f:
        f.write("email: {}, subject: {}, message: {}".format(email, subject, message))