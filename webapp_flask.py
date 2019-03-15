import flask

app=flask.Flask('myapp')

@app.errorhandler(404)
def errorpage(e):
    return 'Page under construction'

@app.route('/')
def homepage():
    return 'Welcome'

@app.route('/<name>')
def aboutpage(name):
    return '<b>about</b>'

@app.route('/emp/<int:id>')
def empid(id):
    return 'your id:' + str(id)

@app.route('/path/<path:p>')
def fullpath(p):
    return 'path received:' + str(p)

#@app.route('/reg/<r:re:[a-z0-9]+>') # regex not supported in Flask
#def regex(r):
#    return 'Received:' + str(r)

@app.route('/red')
def red():
    return flask.redirect('https://www.google.com')

@app.route('/login')
def loginpage():
    return '''<form action='/verifylogin' method='post'>
        User Name: <input type='text'name='uname' /> <br>
        Password: <input type='password'name='pw' /> <br>
        <input type='submit' value='Login' />
    </form>
    '''

@app.route('/verifylogin', methods=['get','post'])
def vlogin():
    u=flask.request.form.get('uname')
    p=flask.request.form.get('pw')
    if not (u == 'abc' and p == 'xyz'):
        return 'Login Failed'
    else:
        return 'Login Success'

app.run(host='192.168.190.1',port=45678)


# flask template
# .html
# {% for %}
# {% endfor%}
#{{var}}