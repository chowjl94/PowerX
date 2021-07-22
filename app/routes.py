
from flask import render_template
from flask import request
from app import application



@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='Mini Project 1 Home')

@application.route('/ex1')
def exercise1():
    return render_template('ex1.html', title='Mini Project 1 Exercise 1')

@application.route('/ex2', methods = ['GET','POST'])
def exercise2():
    num_seq = request.args.get("numbers")
    return render_template('ex2.html', title='Mini Project 1 Exercise 2', numbers = num_seq )