
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import os
from sklearn.externals import joblib
import json
app = Flask(__name__)


model = joblib.load('model.pkl')

def Convert(user_input):
    inputed = pd.DataFrame([user_input])
    cleaned_df = pd.read_csv('cleaned_df.csv')
    test_df = cleaned_df.append(inputed, ignore_index=True, sort=True)
    sklearn_df_test=pd.get_dummies(test_df, columns=[ 'model', 'make', 'transmission', 'fuel', 'body_style'],drop_first=True)
    df_sk_x_test=sklearn_df_test.drop(['price'], axis = 1)
    testing = df_sk_x_test.iloc[[-1]]

    
    pred_t=model.predict(testing)
    return int(pred_t)
        
        

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    result = request.form
    #print(type(d))
    
    milage = result['milage']
    model = result['model']
    make = result['make']
    transmission = result['transmission']
    fuel = result['fuel']
    Num_Cyl = result['Num_Cyl']
    year = result['year']
    body_style = result['body_style']
    
    user_input = {'milage': milage, 'model':model , 'make':make, 'transmission': transmission,'fuel':fuel, 'Num_Cyl':Num_Cyl, 'year':year, 'body_style':body_style}
    print(user_input)
    pred=Convert(user_input)
    
    return render_template('result.html', prediction_text="Your used car's price should be ₦{:.2f} ".format(float(pred)*250))

@app.route('/api',methods=['POST'])
def predicts():
    result = request.form
    #print(result)
    milage = result['milage']
    model = result['model']
    make = result['make']
    transmission = result['transmission']
    fuel = result['fuel']
    Num_Cyl = result['Num_Cyl']
    year = result['year']
    body_style = result['body_style']
    prediction_timeline = result['prediction_timeline']
    
    curacel = 'curacel'
    password = 'password'
    user_input = {'milage': milage, 'model':model , 'make':make, 'transmission': transmission,'fuel':fuel, 'Num_Cyl':Num_Cyl, 'year':year, 'body_style':body_style}
    print(user_input)    

    if (result['username'] == curacel or result['password'] == password):
        pred1=Convert(user_input)
        pred = ({'price':"Your used car's price should be {:.2f} Naira".format((pred1)*250)})
        
    else: 
        pred = "Pls enter the correct password"

    return json.dumps(pred)

if __name__ == "__main__":
    app.run(debug=True)