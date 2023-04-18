from flask import Flask, session, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import pickle
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'predictingrespimbalance'
model = pickle.load(open('model.pkl', 'rb'))
app.secret_key = 'predictingrespimbalance'

# Connect to MongoDB Atlas
MONGODB_URI = "mongodb+srv://josephsamuelm2021:Samenoch%4074@cluster0.itztqvl.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)
db = client['patients']


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # get the user's data from the signup form
        email = request.form['email']
        pid = request.form['pid']
        password = request.form['password']

        # Insert user's data into database
        db.patient_details.insert_one(
            {"email": email, "pid": pid, "password": password})

        # redirect the user to login page
        return redirect(url_for('home'))

    # if the request method is GET,  render the signup page template
    return render_template('signup.html')

# Define a route for the index page


@app.route('/index')
def index():
    if 'pid' in session:
        return render_template('index.html')
    else:
        return redirect('/login')

# Defining a route for the login page


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Getting the patient data
        pid = request.form['pid']
        password = request.form['password']

        # checking if the patient's credentials are valid
        user = db.patient_details.find_one({'pid': pid, 'password': password})
        if user is not None:
            session['pid'] = pid
            # if credentials are valid, redirecting to index page
            return redirect(url_for('index'))
        else:
            # if credentials are invalid,showing an error message
            # return redirect("/signup")

            flash('Invalid Patient ID or Password. Please Try again.')
    # if the request method is GET, render the login page
    return render_template('login.html')

# For logout


@app.route('/logout')
def logout():
    session.pop('pid', None)
    # redirect to login page
    return redirect(url_for('login'))

# To use the predict button in our web-app


@app.route('/predict', methods=['POST'])
def predict():
    # For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    return render_template('index.html', prediction_text='The patient has {} Respiratory Imbalance '.format(prediction))


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
   # app.run(debug=True)
