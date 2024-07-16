from flask import Flask, render_template, url_for, request, jsonify
import joblib

model = joblib.load('rfmodel.lb')
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inputdata')
def inputdata():
    return render_template('input_data.html')

@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        ne=0
        nw=0
        se=0
        sw=0
        
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        bmi = int(request.form['bmi'])
        
        region = request.form['region']
        if region == 'ne':
            ne=1
        elif region == 'nw':
            nw=1
        elif region == 'se':
            se=1
        elif region == 'sw':
            sw=1

        smoke = int(request.form['smoke'])
        children = int(request.form['children'])
        # data = {
        #     'Age': age,
        #     'Gender': gender,
        #     'BMI': bmi,
        #     'Region': region,
        #     'Smoke': smoke,
        #     'Children': children,
        # }
        user_data = [[age, gender, bmi,children, smoke, ne, nw, se, sw] ]

        pred = model.predict(user_data)[0]

        return render_template('prediction.html', output=str(pred))

if __name__ == '__main__':
    app.run(debug=True)
