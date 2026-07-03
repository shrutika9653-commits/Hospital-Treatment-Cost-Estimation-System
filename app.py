import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.title(" Hospital Treatment Cost Estimation System")
df = pd.read_csv("final_insurance.csv")
model = pickle.load(open("model.pkl","rb"))

#sex = sorted(df['sex'].unique())

age = st.sidebar.number_input("Enter age", min_value = 10, max_value = 99, step = 1)
sex = st.sidebar.selectbox("Select Gender",["Male","Famale"])
bmi = st.sidebar.number_input("Enter bmi", min_value = 15.00, max_value = 55.00, step = 0.1)
children = st.sidebar.number_input("Enter children", value = 0, min_value = 0, max_value = 10, step = 1)
#smokers = sorted(df[df['age'] == age]['smoker'].unique())
smoker = st.sidebar.selectbox("Select smoker",["Yes","No"])
region = st.sidebar.selectbox("Select region",["southwest","southeast","northwest","northeast",])


if st.sidebar.button("Predicted charges"):
    st.write("Predicting for")
    st.write("age: ", str(age))
    st.write("sex: ", sex)
    st.write("bmi: ", str(bmi))
    st.write("children: ", str(children))
    st.write("smoker: ", smoker)
    st.write("region: ", region)
    

    columns = ['age', 'sex', 'bmi', 'children', 'smoker','region']
    myinput = [[age, sex, bmi, children, smoker,region]]
    myinput = pd.DataFrame(data = myinput, columns = columns)
    st.write(myinput)
    result = model.predict(myinput)
    if result[0,0] < 0:
        st.error("Sorry, inputs are wrong.")
    else:
        st.success("Predicted Charges:" + str(round(result[0,0])))
