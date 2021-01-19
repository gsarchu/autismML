#Loading the required libraries
import streamlit as st
import pandas as pd
import numpy as np
#import plotly.express as px
#from plotly.subplots import make_subplots
#import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

#Calling the model we saved above:

pickle_in = open('asd_svm.pkl', 'rb')
classifier = pickle.load(pickle_in)
#Creating the UI for the application:


st.markdown("<h1 style='text-align: center; color: red;'>Analysis of Autism Trend data</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>Modeller : Archana Girinath </h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: blue;'><href>https://github.com/gsarchu/autismML</href></h4>",unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>Autism Screening Questionnare </h2>", unsafe_allow_html=True)
A1= st.selectbox("1. Does your child look at you when you call his/her name? ", [False, True])
A2= st.selectbox("2. How easy is it for you to get eye contact with your child? ", [False, True])
A3= st.selectbox("3. Does your child point to indicate that s/he wants something? (e.g. a toy that is out of reach) ", [False, True])
A4= st.selectbox("4. Does your child point to share interest with you? (e.g. poin9ng at an interes9ng sight) ", [False, True])
A5= st.selectbox("5. Does your child pretend? (e.g. care for dolls, talk on a toy phone)  ", [False, True])
A6= st.selectbox("6. Does your child follow where you’re looking? ", [False, True])
A7= st.selectbox("7. If you or someone else in the family is visibly upset, does your child show signs of wan9ng to comfort them? ", [False, True])
A8= st.selectbox("8. Would you describe your child’s first words as: ", [False, True])
A9= st.selectbox("9. Does your child use simple gestures? (e.g. wave goodbye)  ", [False, True])
A10= st.selectbox("10. Does your child stare at nothing with no apparent purpose? ", [False, True])

if not A1:
	A1=0
else:
	A1=1
if not A2:
	A2=0
else:
	A2=1
if not A3:
	A3=0
else:
	A3=1
if not A4:
	A4=0
else:
	A4=1
if not A5:
	A5=0
else:
	A5=1
if not A6:
	A6=0
else:
	A6=1

if not A7:
	A7=0
else:
	A7=1
if not A8:
	A8=0
else:
	A8=1
if not A9:
	A9=0
else:
	A9=1
if not A10:
	A10=0
else:
	A10=1



submit = st.button('Submit')
if submit:
	prediction = classifier.predict([[A2, A5, A6, A9, A7, A1, A4, A3, A8]])
	if prediction ==1:
		st.write("Your child could be Autistic (with an accuracy of 96.2%) ")
	else:
		st.write("Analysis shows that your child is not autistic (with an accuracy of 96.2%)")	

