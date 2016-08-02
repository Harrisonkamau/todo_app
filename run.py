#!/usr/bin/env python

# import flask module
from flask import Flask, render_template, request, url_for, json


# create a Flask Constructor
app = Flask(__name__)


# Create a home route using python decorators
@app.route('/')
def index():
    return render_template('index.html')


# create a showSignUp route
@app.route('/showSignUp')
def show_sign_up():
    # render the sign up page
    return render_template('signup.html')


# create a signup route
@app.route('/signUp', methods=['POST'])
def sign_up():

    # read the values posted on the signup
    name = request.form['inputName']
    email = request.form['inputEmail']
    password = request.form['inputPassword']

    # validate the received values
    if name and email and password:
        return json.dumps({'html':'<span>Details verified!</span>'})
    else:
        return json.dumps({'html': '<span>Enter all the required details!</span>'})

if __name__ == "__main__":
    app.run(debug=True)
