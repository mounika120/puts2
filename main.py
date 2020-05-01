from flask import Flask, request
from fractions import Fraction
from decimal import Decimal

app = Flask(__name__)

@app.route('/')
def index():
    return 'div num1/num2'


@app.route('/div')
def Division():
    num1=request.args.get('A',default = 0, type = Fraction)
    num2=request.args.get('B',default = 0, type = Fraction)
    num3= Fraction(num1)
    num4= Fraction(num2)
    X=num3/num4
   
    Z = str(X).split('/')
    if len(Z) == 2:
        num5 = int(Z[0])/int(Z[1])
        num6= str(num5).split('.')
        if num6[1] == '0':
            return '$ \n'% num6[0]
        else:
            return '$ \n' % num5
    else:
        result1=str(X).split('.')
        return '$ \n'% result1[0]


if __name__ == "__main__":
    app.run()