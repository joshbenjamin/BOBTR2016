from flask import Flask, redirect, url_for, render_template, json, request

app = Flask(__name__)

@app.route('/')                           # Just reroutes the default address to the welcome page
def index():
    return redirect(url_for('welcome'))

@app.route('/Welcome')
def welcome():
    options = ["Sex", "Class", "Age"]     # Options for data to be viewed
    return render_template('welcome.html', options=options)

@app.route('/data/<category>', methods=['GET', 'POST'])
def front(category):
    names = []
    num_entries = len(request.json)

    if category == 'Sex':
        num_males = 0
        num_females = 0
        survived_males = 0
        survived_females = 0

        for i in range(0, num_entries):
            if(request.json[i]['sex'] == "male"):
                num_males+=1
                if(request.json[i]['survived'] == "1"):
                    survived_males+=1
            else:
                num_females+=1
                if (request.json[i]['survived'] == "1"):
                    survived_females += 1


    #print ("Total: ", num_entries, "\n", "Males: ", num_males, "\n", "Females: ", num_females)
    print "Total: ", num_entries
    print "Males: ", num_males
    print "Number of Survivors: ", survived_males
    print "Females: ", num_females
    print "Number of Survivors: ", survived_females

    return render_template('data.html', category=category)


if __name__ == '__main__':
    app.run(debug=True)
