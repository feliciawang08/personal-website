from flask import Flask, render_template, url_for, redirect, request
import csv
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

# handles contact form submission
@app.route('/form_submission_success', methods = ['GET','POST'] )
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            message = 'form submitted! i will get back to you as soon as possible.'
            return render_template('formsubmitted.html',message=message)
        except:
            message = "did not save information to database."
            return render_template('formsubmitted.html',message=message)
    else:
        message = "you didn't submit a form."
        return render_template('formsubmitted.html', message=message)

# writes contact information to csv file
def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data["message"]
    with open('db.csv', 'wb') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])