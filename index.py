from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	return redirect(url_for('add')) #導向add 重導向request

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST': #request
        a=request.form['adder1'] #request
        b=request.form['adder2'] #request
        a=int(a)
        b=int(b)
        c=a+b
        return render_template("index.html",adder1=str(a),adder2=str(b),message=str(c)) # render_template
    return render_template("index.html") # render_template

if __name__=='__main__':
	app.run('0.0.0.0',port=80)