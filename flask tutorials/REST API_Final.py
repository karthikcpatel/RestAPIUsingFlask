from flask import Flask, request
app = Flask(__name__)

in_memory_datastore = {
   "top_reasons" : {"ExternalRecommendation": 0.25, "WorkHours": 0.50, "SurveyResponse": 0.75, "ChatEmail": 1.0 },
   "stress_distribution" : {"Depressed": 0.25, "Stressed": 0.50, "Normal": 0.75, "Happy": 1.0 },
}

@app.route('/')
def hello_mitr():
    """This function will be executed when the server is started.
    """
    return "Welcome MITR!"

@app.get('/different_parameters')
def different_parameters():
   return {"different_parameters":list(in_memory_datastore.values())}

@app.route('/different_parameters/<parameter_name>')
def get_programming_language(parameter_name):
   return in_memory_datastore[parameter_name]

if __name__ == '__main__':
    app.run(debug=True)