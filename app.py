from flask import Flask , request
app = Flask(__name__);

@app.route("/")
def index():
    return "<b> Mansh raj</b>"

@app.route('/manash/<name>')
def manash(name):
    return f"my mae is {name}"

@app.route('/manash/<int:num1>/<int:num2>')
def man(num1,num2):
    return f"{num1}+{num2} = {num1+num2}"

@app.route('/manas/<num1>/<num2>')
def mani(num1,num2):
    a=int(num1)
    b=int(num2)
    return f"{num1}+{num2}={a+b}"

@app.route('/name')
def mana():
    if 'a' in request.args.keys() and  'b' in request.args.keys():
       a=request.args.get('a');
       b=request.args.get('b');
       return f"name={a},age={b}"
    else:
        return "No header found"
    


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)
    