import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() 
    return redirect(url_for('renderMain')) 

@app.route('/page1')
def renderPage1():
    
    return render_template('page1.html')
@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if "firstanswer" not in session:
        session["firstanswer"]=request.form['firstanswer']
    return render_template('page2.html')

@app.route('/page4',methods=['GET','POST'])
def renderPage4():
 if "secondanswer" not in session:
    session["secondanswer"]=request.form['secondanswer']
 return render_template('page4.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "thirdanswer" not in session:
        session["thirdanswer"]=request.form['thirdanswer']
    c = 0
    if session["firstanswer"]== "JavaScript":
        first= "correct"
        c = 1
    else:
        first= "wrong"
    if session["secondanswer"]== "2500":
        second= "correct"
        c = c + 1
    else:
        second= "wrong"
    if session["thirdanswer"]== "40":
        third= "correct"
        c = c + 1
    else:
        third= "wrong"
    
    return render_template('page3.html',score=c,first=first,second=second,third=third)
    
    
if __name__=="__main__":
    app.run(debug=True)