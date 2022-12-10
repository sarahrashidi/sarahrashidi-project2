from flask import Flask
from flask.json import jsonify
from flask import request

app = Flask(__name__)

@app.route("/background")
def background():
    return ["System Administrator @Accenture","Operations Manager @Accenture","DevOps Engineer @Snyk"]

@app.route("/email")
def get_email():
    return jsonify("student@youarethebest.com")

@app.route("/zip")
def get_zip():
    return jsonify("40000")

@app.route("/name")
def get_employee_name():
    return jsonify("Elon Musk")

@app.route("/programOfStudy")
def get_degree_study_path():
    return {
        'degree': "Master",
        'study_program': "DevOps & Site Reliability Program"
    }

@app.route("/skills")
def get_skills():
    return [
        {
            'key'  : 'Programming languages',
            'value': ['Java','Go','Python'] 
        },
         {
            'key'  : 'Scripting languages',
            'value': ['Perl','Bash'] 
        }
    ]

@app.route("/topics")
def get_topics():
    return {
  "1": "Kubernetes",
  "2": "Cloud Native Applications",
  "3": "Cloud Computing",
}

@app.route("/advance/device_name",methods = ['POST'])
def get_device_name():
    devices = list(request.json['device_names'])
    ordred_devices = []
    if len(devices) == 0 :
        return None
    else:
        keywords = set()
        result_set = set()
        for word in devices :
            keywords.add(word)
        for word in keywords :
            i = 0
            for entry in devices:
                if word == entry and entry in result_set:
                    i = i+1
                    result_set.add(f"{word}{i}")
                elif word == entry :
                    result_set.add(word)
                else:
                    continue
        ordred_devices = list(result_set)
        ordred_devices.sort()
        return ordred_devices
    
