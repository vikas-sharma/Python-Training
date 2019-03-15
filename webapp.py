import bottle
#import flask
# import django
# import web2py

import sqlite3
import json

app = bottle.Bottle()

@app.error(404)
def errorpage(e):
    return 'Page under construction'

@app.route('/')
def homepage():
    return 'Welcome'

@app.route('/<name>')
def aboutpage(name):
    return '<b>about</b>'

@app.route('/emp/<id:int>')
def empid(id):
    return 'your id:' + str(id)

@app.route('/path/<p:path>')
def fullpath(p):
    return 'path received:' + str(p)

@app.route('/reg/<r:re:[a-z0-9]+>') # not supported in Flask
def regex(r):
    return 'Received:' + str(r)

@app.route('/red')
def red():
    return bottle.redirect('https://www.google.com')

@app.route('/login')
def loginpage():
    return '''<form action='/verifylogin' method='post'>
        User Name: <input type='text'name='uname' /> <br>
        Password: <input type='password'name='pw' /> <br>
        <input type='submit' value='Login' />
    </form>
    '''

@app.post('/verifylogin')
def vlogin():
    u=bottle.request.forms.get('uname')
    p=bottle.request.forms.get('pw')
    if not (u == 'abc' and p == 'xyz'):
        return 'Login Failed'
    else:
        con = sqlite3.connect('mydb.sqlite3')
        cur = con.cursor()
        cur.execute('SELECT * from LOGDATA')
        result = cur.fetchall()
        print (bottle.TEMPLATE_PATH)
        bottle.TEMPLATE_PATH.append(r'C:\vikas\bin')
        return bottle.template('report.tpl', res=result)

@app.route('/json')
def jsondata():
    D={'A':10,'B':20}
    F=open('mydata.json', 'w')
    json.dump(D,F)
    F.close()

    F=open('mydata.json')
    r=json.load(F)
    F.close()
    return r

@app.route('/download/<fname>')
def staticfile(fname):
    return bottle.static_file(fname, root=r'C:\vikas\bin')

@app.route('/ai/ml')
def ml():
    return bottle.template('report2.tpl')

@app.post('/submitdata')
def readdata():
    p1 = bottle.request.forms.get('p1')
    p2 = bottle.request.forms.get('p2')
    p3 = bottle.request.forms.get('p3')
    p4 = bottle.request.forms.get('p4')

    import ml_ex
    res = ml_ex.getresult(p1,p2,p3,p4)
    return ml_ex.numToString(res)

app.run(host='192.168.190.1',port=45678)


#bottle template
# .tpl -- template engine extension
# %for
# %end
# {{variable}}