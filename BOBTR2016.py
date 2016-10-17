from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def redirect():
    return redirect('localhost:5000/Welcome')

@app.route('/Welcome')
def hello_world():
    #options = ['<a href="/first">First<a>', '<a href="/second">Second<a>', '<a href="/third">Third<a>']
    options = ["Sex", "Class", "Age"]
    return render_template('welcome.html', options=options)
    #return 'Hello World! Go to <a href="/yes">Click here<a>'

@app.route('/yes')
def nextpage():
    return "You are here"


#@app.route('/data/Sex')
#@app.route('/data/Class')
#@app.route('/data/Age')
@app.route('/data/<category>')
def front(category):
    return 'To go back, simply <a href="/Welcome">Click Here<a>'


if __name__ == '__main__':
    app.run(debug=True)
