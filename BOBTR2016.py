from flask import Flask, redirect, url_for, render_template, json, request
import requests

app = Flask(__name__)

url = "http://titanic.businessoptics.biz/survival/"

@app.route('/')                           # Just reroutes the default address to the welcome page
def index():
    return redirect(url_for('welcome'))

@app.route('/Welcome')
def welcome():
    options = ["Sex", "Class", "Age", "Embarkation Port"]     # Options for data to be viewed
    return render_template('welcome.html', options=options)

@app.route('/data/<category>', methods=['GET', 'POST'])
def data(category):
    request_info = requests.get(url)
    text_representation = request_info.text
    data = json.loads(text_representation)

    num_entries = len(data)

    if category == 'Sex':
        num_males = 0
        num_females = 0
        survived_males = 0
        survived_females = 0

        for i in range(0, num_entries):
            if(data[i]['sex'] == "male"):
                num_males+=1
                if(data[i]['survived'] == "1"):
                    survived_males+=1
            else:
                num_females+=1
                if (data[i]['survived'] == "1"):
                    survived_females += 1

        survived_all = survived_males + survived_females

        percentage_males = int(100 * (float(survived_males) / float(num_males)))
        percentage_females = int(100 * (float(survived_females) / float(num_females)))
        percentage_all = int(100 * (float(survived_all) / float(num_entries)))

        values = [num_males, num_females, num_entries, survived_males, survived_females,
                  (survived_males + survived_females), percentage_males, percentage_females, percentage_all]

        return render_template('sex.html', category=category, values=values)


    elif category == 'Age':
        age_groups = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 'unknown': 0}
        survived_ages = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 'unknown': 0}
        percentage_ages = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 'unknown': 0}

        for i in range(0, num_entries):
            if (data[i]['age'] != ""):
                current_age = int(float(data[i]['age']))
                for key in age_groups.iterkeys():
                    if current_age <= ((key+1)*10):
                        age_groups[key]+=1
                        if (data[i]['survived'] == "1"):
                            survived_ages[key]+=1
                        break
            else:
                age_groups['unknown']+=1

        for key in age_groups.iterkeys():
            percentage_ages[key] = int(100 * (float(survived_ages[key]) / float(age_groups[key])))

        return render_template("age.html", category=category, age_groups=age_groups, survived_ages=survived_ages, percentage_ages=percentage_ages)


    elif category == 'Class':
        class_groups = {1:0, 2:0, 3:0}
        class_survived = {1:0, 2:0, 3:0}
        class_percentage = {1:0, 2:0, 3:0}

        for person in data:
            person_class = int(person['class'])
            class_groups[person_class]+=1
            if person['survived'] == "1":
                class_survived[person_class]+=1

        for key in range (1, 4):
            class_percentage[key] = int(100 * (float(class_survived[key]) / float(class_groups[key])))

        print str(class_groups)
        print str(class_survived)
        print str(class_percentage)


        #return "Success"

        return render_template("class.html", category=category, class_groups=class_groups, class_survived=class_survived, class_percentage=class_percentage)


    elif category == "Embarkation Port":
        ports = {}
        ports_survived = {}
        ports_percentage = {}

        for person in data:
            current_embark = str(person['Embarked'])
            if current_embark == "":
                current_embark = "Unknown"

            if current_embark not in ports:
                ports[current_embark] = 0
                ports_survived[current_embark] = 0
                ports_percentage[current_embark] = 0
            ports[current_embark]+=1
            if person['survived'] == "1":
                ports_survived[current_embark]+=1

        for key in ports.iterkeys():
            ports_percentage[key] = int(100 * (float(ports_survived[key]) / float(ports[key])))


        return render_template("embarkation.html", category=category, ports=ports, ports_survived=ports_survived, ports_percentage=ports_percentage)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
