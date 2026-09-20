import streamlit as st
import pickle
import pandas as pd

# Load the trained Decision Tree model
with open("Churn_decision_tree.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("📊 Telecom Customer Churn Prediction")

st.write("Enter customer details to predict whether the customer is likely to churn.")

# Customer inputs
AccountWeeks = st.number_input("Account Weeks", min_value=0, value=100)
ContractRenewal = st.selectbox("Contract Renewal", [0, 1])
DataPlan = st.selectbox("Data Plan", [0, 1])
DataUsage = st.number_input("Data Usage", min_value=0.0, value=2.0)
CustServCalls = st.number_input("Customer Service Calls", min_value=0, value=1)
DayMins = st.number_input("Day Minutes", min_value=0.0, value=180.0)
DayCalls = st.number_input("Day Calls", min_value=0, value=100)
MonthlyCharge = st.number_input("Monthly Charge", min_value=0.0, value=50.0)
OverageFee = st.number_input("Overage Fee", min_value=0.0, value=10.0)
RoamMins = st.number_input("Roaming Minutes", min_value=0.0, value=10.0)

# Prediction button
if st.button("Predict Churn"):

    input_data = pd.DataFrame([[
        AccountWeeks,
        ContractRenewal,
        DataPlan,
        DataUsage,
        CustServCalls,
        DayMins,
        DayCalls,
        MonthlyCharge,
        OverageFee,
        RoamMins
    ]], columns=[
        "AccountWeeks",
        "ContractRenewal",
        "DataPlan",
        "DataUsage",
        "CustServCalls",
        "DayMins",
        "DayCalls",
        "MonthlyCharge",
        "OverageFee",
        "RoamMins"
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🔴 Customer is likely to CHURN")
    else:
        st.success("🟢 Customer is likely to STAY")
