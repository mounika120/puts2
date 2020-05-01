from flask import Flask, request
from fractions import Fraction
from decimal import Decimal
app = Flask(__name__)
@app.route('/')
def index():
    return 'Give the values for A and B in the URL form'
	
@app.route('/add')
def Addition():
    try:
        num1 = request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError:
        num1 = 'None'
    try:
        num2 = request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError:
        num2 = 'None'
    if num1=='None' or num2 == 'None':
        return'Error: please enter valid inputs'
    else:
        num3= Fraction(num1)
        num4= Fraction(num2)
        X = num3+num4
        return str(round(float(X),6))

@app.route('/sub')
def Substraction():
    try:
        num1 = request.args.get('A' , default = 0, type = Fraction)
    except ZeroDivisionError:
        num1 = 'None'
    try:
        num2 = request.args.get('B',default =0, type = Fraction)
    except ZeroDivisionError:
        num2 = 'None'
    if num1 == 'None' or num2 == 'None':
        return'Error: please enter valid inputs'
    else:
        num3= Fraction(arg1)
        num4 = Fraction(arg2)
        X= num3-num4
        return str(round(float(X),6))
        
@app.route('/mul')
def Multiplication():
    try:
        num1 = request.args.get('A' , default=0, type = Fraction)
    except ZeroDivisionError:
        num1 = 'None'
    try:
        num2 = request.args.get('B' , default=0, type = Fraction)
    except ZeroDivisionError:
        num2 = 'None'
    if num1 == 'None' or num2 == 'None':
        return 'Error:please enter valid inputs'
    else:
        num3= Fraction(arg1)
        num4= Fraction(arg2)
        X= num3*num4
        return str(round(float(X),6))
       
@app.route('/div')
def Division():
    try:
        num1 = request.args.get('A' , default=0, type = Fraction)
    except ZeroDivisionError:
        num1= 'None'
    try:
        num2 = request.args.get('B' , default=0, type = Fraction)
    except ZeroDivisionError:
        num2 = 'None'
    if num3 == 'None' or num4 == 'None':
        return 'Error:please enter valid inputs'
    else:
        num3= Fraction(arg1)
        num4= Fraction(arg2)
        X = num3/num4
        return str(round(float(X),6))
    
    
if __name__ == "__main__":
    app.run(debug=True)