#!/usr/bin/env python

# import flask module
from flask import Flask, render_template, redirect


# create a Flask Constructor
app = Flask(__name__)


# Create a route using python decorators
@app.route('/')
def home():
    return "This is home!"


@app.route('/template')
def temp():
    return render_template('template.html')


if __name__ == "__main__":
    app.run(debug=True)
