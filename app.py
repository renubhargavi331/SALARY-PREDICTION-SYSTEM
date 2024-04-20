from flask import Flask,render_template,request
import numpy as np
import pickle

with open("Salary_Prediction.pkl",'rb') as f:
    model = pickle.load(f)
#create an object instance
app = Flask(__name__)
@app.route('/sa')
def check():
    return "Codegnan is in NBKR"
@app.route('/') #by default methods = ['GET']
def new():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def predict():
    Age = int(request.form['Age'])
    Job_Title = int(request.form['Job_Title'])
    Years_of_Experience= int(request.form['Years_of_Experience'])
    gender = int(request.form['gender'])
    Education_Level= int(request.form['Education_Level'])
    input_data = np.array([[Age,Job_Title,Years_of_Experience,gender,Education_Level]])
    predicted_price = model.predict(input_data)[0]
    x=round(predicted_price)
    return render_template('index.html', prediction = x)
app.run()
