import MySQLdb
from flask import Flask,render_template,request, redirect,url_for

app=Flask(__name__)
@app.route('/',defaults={'message':''})
@app.route('/<message>')
def index(message):
    if message=="":
        return render_template('home.html',status=message)
    else:
        return render_template('home.html',status=message)

@app.route('/login',defaults={'conflict':''})
@app.route('/login/<conflict>')
def login(conflict):
    if conflict=="":
        return render_template('login.html',status=conflict)
    else:
        return render_template('login.html',status=conflict)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index',message='Bye-Bye'))

@app.route('/result' ,methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        print('in result-----------------')
        first_name=str(request.form['inputfName'])
        last_name=str(request.form['inputlName'])
        email_id=str(request.form['inputEmail'])
        password=str(request.form['inputPassword'])
        db = MySQLdb.connect("localhost", "root", "9700464021Sp@", "TESTDB")
        cursor = db.cursor()
        sql1="Select * from db1 where email_id='%s'"%(str(email_id))
        res=cursor.execute(sql1)
        print(res)
        if res!=0:
            db.close()
            return redirect(url_for('login',conflict="Already registered"))
        else:
            sql="INSERT INTO db1 (first_name,last_name,email_id,password) VALUES('%s','%s','%s','%s')"%(first_name,last_name,email_id,password)
            cursor.execute(sql)
            db.commit()
            db.close()
            return redirect(url_for('index',message="Welcome Aboard : '%s'"%(first_name)))

@app.route('/result1' ,methods = ['POST', 'GET'])
def result1():
    if request.method == 'POST':
        email_id=str(request.form['inputEmail'])
        password=str(request.form['inputPassword'])
        db = MySQLdb.connect("localhost", "root", "9700464021Sp@", "TESTDB")
        cursor = db.cursor()
        sql="Select * from db1 where email_id='%s' and password='%s'"%(str(email_id),str(password))
        cursor.execute(sql)
        results=cursor.fetchall()
        if results:
            return redirect(url_for('index',message="Welcome Aboard : %s"%(results[0][0])))
        else:
            return redirect(url_for('login',conflict="Try Again"))

@app.route('/list',methods=['POST','GET'])
def list():
    if request.method!='POST':
        db = MySQLdb.connect("localhost", "root", "9700464021Sp@", "TESTDB")
        cursor = db.cursor()
        sql="Select * from db1"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            print(results)
        except:
            print("Error: unable to fecth data")
            results = False
        db.close()
        return render_template("result.html",result_data = results)
    else:
        return redirect(url_for('index',message="Welcome Aboard"))

if __name__=='__main__':
    app.run(debug=True)

"""
t=int(raw_input())
while t>0:
    flag=0
    n=int(raw_input())
    for i in range(2,n+1):
        if (n%i)==0:
            flag=i
            break
    print("%d %d"%(flag,n-flag))
    t-=1"""