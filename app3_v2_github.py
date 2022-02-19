# Author: Prakash Sukhwal
# Aug 2021

import streamlit as st
# other libs
import numpy as np
import pandas as pd
import pickle
# import pyautogui # for reset button: pip install pyautogui

# load the model.pkl
#path = r'E:\Oscar\#NUS\NUS study\DSSI - Data Science Solution Implementation\Lecture Material\Day 2\Code files\DSSI Day 2 Workshop\model.pkl'
with open('model.pkl', "rb") as f:
	model = pickle.load(f)

# Streamlit provides a caching mechanism that allows your app to stay performant 
# even when loading data from the web, manipulating large datasets, 
# or performing expensive computations. This is done with the @st.cache decorator.
@st.cache()

def prediction(age, km, hp, automatic, cc, doors, weight, diesel, petrol):
	# Making predictions
	prediction = model.predict([[age, km, hp, automatic, cc, doors, weight, diesel, petrol]])
	return prediction


# putting the app related codes in main()
def main():
	# -- Set page config
	apptitle = 'DSSI'
	st.set_page_config(page_title=apptitle, page_icon='random', 
		layout= 'wide', initial_sidebar_state="expanded")
	# random icons in the browser tab

	# give a title to your app
	st.title('Solution Implementation')
	#front end elements of the web page 
	# pick colors from: https://www.w3schools.com/tags/ref_colornames.asp
	html_temp = """ <div style ="background-color:AntiqueWhite;padding:15px"> 
       <h1 style ="color:black;text-align:center;">A car price prediction app</h1> 
       </div> <br/>"""

    #display the front end aspect
	st.markdown(html_temp, unsafe_allow_html = True)
	# let us make infrastructure to provide inputs
	# we will add the inputs to side bar
	st.sidebar.info('Provide input using the panel')
	st.info('Click Assess button below')


	################ declare inputs for UI #####################
	age = st.sidebar.number_input('age')
	st.write('input age of the car', age)

	km = st.sidebar.number_input('km')
	st.write('distance ran in kms', km)

	hp = st.sidebar.number_input('hp')
	st.write('horsepower', hp)

	automatic = st.sidebar.number_input('automatic')
	st.write('1 or 0', automatic)

	cc = st.sidebar.number_input('cc')
	st.write('vehicle fuel capacity', cc)

	doors = st.sidebar.number_input('doors')
	st.write('2/3/4/5 doors', doors)

	weight = st.sidebar.number_input('weight')
	st.write('weight of vehicle', weight)

	diesel = st.sidebar.number_input('diesel')
	st.write('disel 10; petrol 01; CNG 00', diesel)

	petrol = st.sidebar.number_input('petrol')
	st.write('disel 10; petrol 01; CNG 00', petrol)

	result =""
	# assessment button
	if st.button("Predict"):
		assessment = prediction(age, km, hp, automatic, cc, doors, weight, diesel, petrol)
		st.success('**The price of the car is predicted to be:** {}'.format(assessment))

	# if st.button("Reset"):
	# 	pyautogui.hotkey("ctrl","F5")

	# st.balloons()
	st.success("App is working!!") # other tags include st.error, st.warning, st.help etc.

if __name__ == '__main__':
	main()
