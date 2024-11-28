

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

loaded_model=pickle.load(open('trained_model.sav','rb'))

heart_disease_model=pickle.load(open('trained_heart_model.sav','rb'))



with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',],
                           default_index = 0)

if (selected == 'Diabetes Prediction'):
    st.title('diabetes prediction web app')
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies= st.text_input('number of pregnancies')
    with col2:
        Glucose= st.text_input('glucose level')
    with col3:
        BloodPressure= st.text_input('blood pressure level')
    with col1:
        SkinThickness= st.text_input('skinthickness level')
    with col2:
        Insulin= st.text_input('insulin level')
    with col3:
        BMI= st.text_input('bmi level')
    with col1:
        DiabetesPedigreeFunction= st.text_input('diabetespedigressfunction level')
    with col2:
         Age= st.text_input('age of the person')
    
    diagnosis= ''
    
    if st.button('diabetes final results'):
        predict=loaded_model.predict([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        if predict==0:
            diagnosis='no diabetes'
        else:
            diagnosis='diabetes'
    st.success(diagnosis)
    
    
if (selected == 'Heart Disease Prediction'):
    st.title('heart disease prediction web app')
    col1,col2,col3 = st.columns(3)
    with col1:
        trestbps= st.text_input('trestbps')
    with col2:
        chol= st.text_input('chol')
    with col3:
        thalach= st.text_input('thalach')
    with col1:
        age= st.text_input('age')
    with col2:
        sex= st.text_input('sex')
    with col3:
        cp= st.text_input('cp')
    with col1:
        fbs= st.text_input('fbs')
    with col2:
        restecg= st.text_input('restecg')
    with col3:
        exang= st.text_input('exang')
    with col1:
        oldpeak= st.text_input('oldpeak')
    with col2:
        slope= st.text_input('slope')
    with col3:
        ca= st.text_input('ca')
    with col1:
        thal= st.text_input('thal')
    
    diagnosis= ''
    
    if st.button('heart disease final results'):
        heart_predict=heart_disease_model.predict([trestbps,chol,thalach,age,sex, cp, fbs,restecg,exang,oldpeak,slope,ca,thal])
        if heart_predict==0:
            diagnosis='no heart disease'
        else:
            diagnosis='heart disease'
    st.success(diagnosis)

    
    
    
    
