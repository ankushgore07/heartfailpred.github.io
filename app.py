# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 05:40:58 2021

@author: Ankush
"""



from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction
    if prediction== 1:


        return render_template('pred.html', prediction_text='sorry to say that, but you have high Chances of Heart Failure.')
    else:
        return render_template('pred.html', prediction_text='Your Heart is Healthy and dont need to worry about it.')



if __name__ == "__main__":
    app.run(debug=True) 