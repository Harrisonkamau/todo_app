#!/usr/bin/env python

# import flask module
from flask import Flask, render_template, request, url_for


# create a Flask Constructor
app = Flask(__name__)


# Create a route using python decorators
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
