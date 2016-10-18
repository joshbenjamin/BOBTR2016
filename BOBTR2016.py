from flask import Flask, redirect, url_for, render_template, json, request

app = Flask(__name__)

@app.route('/')                           #Just reroutes the default address to the welcome page
def index():
    return redirect(url_for('welcome'))

@app.route('/Welcome')
def welcome():
    options = ["Sex", "Class", "Age"]  # Options for data to be viewed
    return render_template('welcome.html', options=options)

@app.route('/data/<category>')
def front(category):
    total = 0
    count = 0

    #name = request.json['name']


    return render_template('data.html', category=category)


if __name__ == '__main__':
    app.run(debug=True)
