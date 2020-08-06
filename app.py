from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np

 

app = Flask(__name__)

 

model = pickle.load(open('rf_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('loan_type.html')
        
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Loan_Amount_Requested = int(request.form.get('Loan_Amount_Requested',False))
        Length_Employed = int(request.form.get('Length_Employed',False))
        Home_Owner = int(request.form.get('Home_Owner',False))
        Annual_Income = int(request.form.get('Annual_Income',False))
        Months_Since_Deliquency = int(request.form.get('Months_Since_Deliquency',False))
        Income_Verified = int(request.form.get('Income_Verified',False))
        Purpose_Of_Loan = int(request.form.get('Purpose_Of_Loan',False))
        Debt_to_Income = int(request.form.get('Debt_to_Income',False))
        Inquiries_Last_6Mo = int(request.form.get('Inquiries_Last_6Mo',False))
        Number_Open_Accounts = int(request.form.get('Number_Open_Accounts',False))
        Total_Accounts = int(request.form.get('Total_Accounts',False))
        Gender = int(request.form.get('Gender',False))
        No_invalid_accounts = Total_Accounts - Number_Open_Accounts
        prediction=model.predict([[Loan_Amount_Requested, Length_Employed, Home_Owner, Annual_Income, Income_Verified, Purpose_Of_Loan, Debt_to_Income, Inquiries_Last_6Mo, Months_Since_Deliquency, Number_Open_Accounts, Total_Accounts, Gender, No_invalid_accounts]])
        output=prediction[0]
        return render_template('loan_type.html',prediction_text="You Fall into category:-  {}".format(output))
    else:
        return render_template('loan_type.html')
        
if __name__=="__main__":
    app.run(debug=True, use_reloader=False)