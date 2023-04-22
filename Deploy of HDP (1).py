#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# In[17]:


heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))


# In[18]:


with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          
                          ['Heart Disease Prediction'
                          ],
                          icons=['heart'],
                          default_index=0)


# In[19]:


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('age')
        
    with col2:
        sex = st.text_input('sex')
        
    with col3:
        cp = st.text_input('cp')
        
    with col1:
        trestbps = st.text_input('trestbps')
        
    with col2:
        chol = st.text_input('chol')
        
    with col3:
        fbs = st.text_input('fbs')
        
    with col1:
        restecg = st.text_input('restecg')
        
    with col2:
        thalach = st.text_input('thalach')
        
    with col3:
        exang = st.text_input('exang')
        
    with col1:
        oldpeak = st.text_input('oldpeak')
        
    with col2:
        slope = st.text_input('slope')
        
    with col3:
        ca = st.text_input('ca')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)


# In[ ]:




