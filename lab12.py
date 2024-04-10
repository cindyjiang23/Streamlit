import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_csv('car_data.csv')
    return data

data = load_data()

car_name = st.sidebar.text_input('Car Name')

transmission_type = st.sidebar.multiselect('Choose Transmission Type',
                                          ['Manual', 'Automatic'],
                                          default=['Manual', 'Automatic'])

selling_price_range = st.sidebar.slider('Select a range of selling price',
                                       0, 20, (0, 20))

year_range = st.sidebar.slider('Select a range of year',
                               2000, 2024, (2000, 2024))

submit = st.sidebar.button('Submit')

if submit:
    filtered_data = data.copy()
    if car_name:
        filtered_data = filtered_data[filtered_data['car_name'].str.contains(car_name, case=False)]
    if transmission_type:
        filtered_data = filtered_data[filtered_data['transmission'].isin(transmission_type)]
    filtered_data = filtered_data[filtered_data['selling_price'].between(selling_price_range[0], selling_price_range[1])]
    filtered_data = filtered_data[filtered_data['year'].between(year_range[0], year_range[1])]
    
    st.write(filtered_data)
else:
    st.write(data)
        

