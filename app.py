from flask import Flask, request, jsonify
from joblib import load

from Analysis.masters import location_based_colleges, marks_based_colleges
masters_dataset = './Datasets/data.csv'
masters_model = load('./Models/masters.joblib')

from Analysis.placements import analysis, value_evaluator
placements_dataset = './Datasets/placement.csv'
placements_model = load('./Models/placements.joblib')

from Analysis.cgpa import cgpa_calculator

app = Flask(__name__)

@app.route('/')
def barebones():
    return 'Welcome to Student Performance Analyzer API'

@app.route('/placements', methods = ['GET', 'POST'])
def placement_barebones():
    if request.method == 'POST':
        data = request.get_json()
        X_test = value_evaluator(data)
        y_pred = placements_model.predict([X_test])
        poslos, cgpabasis, skills = analysis(placements_dataset, data)
        return jsonify(predicted_company = y_pred[0],\
            position_location = poslos.to_json(orient='records'),\
            cgpabasis = cgpabasis.to_json(orient='records'), \
            skills = skills.to_json(orient='records'))
    return ''

@app.route('/masters', methods=['GET', 'POST'])
def masters_barebones():
    if request.method == 'POST':
        data = request.get_json()
        marks = data['Marks']
        locations = data['Location']
        if locations == 'Borivali':
            andheri, bandra, dadar, vashi = 0,0,0,0
            borivali = 1
        elif locations == 'Andheri':
            borivali, bandra, dadar, vashi = 0,0,0,0
            andheri = 1
        elif locations == 'Dadar':
            borivali, bandra, andheri, vashi = 0,0,0,0
            dadar = 1
        elif locations == 'Vashi':
            borivali, bandra, dadar, andheri = 0,0,0,0
            vashi = 1
        elif locations == 'Bandra':
            borivali, andheri, dadar, vashi = 0,0,0,0
            bandra = 1
        elif locations == 'Virar':
            andheri, bandra, dadar, vashi = 0,0,0,0
            borivali = 1
        elif locations == 'Kurla':
            borivali, bandra, andheri, vashi = 0,0,0,0
            dadar = 1
        
        marks = int(float(marks))
        y_pred = masters_model.predict([[marks, andheri, bandra, borivali, dadar, vashi]])
        
        colleges_based_on_location = location_based_colleges(masters_dataset, locations)
        colleges_based_on_marks = marks_based_colleges(masters_dataset, marks)

        return jsonify(predicted_college= y_pred[0], \
            colleges_based_on_location=colleges_based_on_location.to_json(orient='records'), \
            colleges_based_on_marks=colleges_based_on_marks.to_json(orient='records'))
    return ''


@app.route('/cgpa_estimator', methods=['GET', 'POST'])
def cgpa_barebones():
    if request.method == 'POST':
        data = request.get_json()
        required, recovery = cgpa_calculator(data)
        return jsonify(required_cgpa=required, number_of_semesters=recovery)
    return ''

if __name__ == '__main__':
    app.run(debug=True)
