import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="TAP : Find an apartment", page_icon=None)
st.markdown("<h1 style = 'text-align:left;'>TAP</h1>",unsafe_allow_html=True)
st.markdown("<h4 style = 'text-align:left;'><i>The Appartment People</i></h4>",unsafe_allow_html=True)

input_form = st.container()
input_form = input_form.form("Form 1")

input_form.write("Enter the details to predict the approximate buying price of your desired apartment")

year_built = input_form.text_input("Which year was the apartment built in? ")
size_sqf = input_form.text_input("What is the total size of the apartment?")
floor = input_form.text_input("Which floor is the apartment unit?")

hallway = input_form.selectbox("Select the Hallway type",options=('terraced', 'corridor', 'mixed'))
heating = input_form.selectbox("Select the type of heating",options=('individual_heating', 'central_heating'))
management = input_form.selectbox("Select the management type for the apartment", options=('management_in_trust', 'self_management'))

parking_ground = input_form.text_input("Enter size of the ground level parking lot")
parking_basement= input_form.text_input("Enter size of the basement parking lot")

nearest_subway = input_form.selectbox("select the nearest subway station", options=(['Kyungbuk_uni_hospital', 'Daegu', 'Sin-nam', 'Myung-duk',
       'Chil-sung-market', 'Bangoge', 'Banwoldang','other', 'no_subway_nearby']))

time_to_subway = input_form.text_input("Enter the approximate time to the nearest subway station")
time_to_bus_stop = input_form.text_input("Enter the approximate time to the nearest bus stop")

num_apts = input_form.text_input("Enter the number of apartment in the building")
num_elevators = input_form.text_input("Enter the number of elevators in the apartment building")
num_hospitals = input_form.text_input("Enter the number of hospital/clinics nearby (<2km radius)")
num_markets = input_form.text_input("Enter the number of markets nearby")
num_malls= input_form.text_input("Enter the number of malls nearby")


sub_button = input_form.form_submit_button("SUBMIT")


