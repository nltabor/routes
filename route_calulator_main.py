import streamlit as st
import numpy as np

col1, col2 = st.columns(2)

def manual(input_wage, input_miles, input_time, total_stops, gas, mpg):
    average_stop_time = 5  # holder for average amount of time spent per stop
    stops_time = (total_stops * average_stop_time) / 60
    trip_time = input_time / 60
    a = np.round((input_miles / mpg) * gas, 2)  # cost of miles
    b = np.round((trip_time + stops_time) * input_wage, 2)  # cost of labor
    d = np.round(a / b, 2)  # ratio between miles and labor
    cost = np.round(a + b, 2)
    with col2:
        st.markdown('### results:')
        st.markdown('### ')
        st.markdown('##### ------------------------------------------------- ')
        st.markdown(str('##### route cost ') + str(cost))
        st.markdown('##### ------------------------------------------------- ')
        st.markdown(str('##### gas cost ') + str(a))
        st.markdown('##### ------------------------------------------------- ')
        st.markdown(str('##### labor cost ') + str(b))
        st.markdown('##### ------------------------------------------------- ')
        st.markdown(str('##### stops_time ') + str(round(stops_time,2)))
        st.markdown('##### ------------------------------------------------- ')
        st.markdown(str('##### trip_time ') + str(round(trip_time,2)))
        st.markdown('##### ------------------------------------------------- ')

#st.title('Hardy Route Calculator')
form_main = st.form('main')
with form_main:
    with col1:
        gas = st.number_input('current omaha gas average')
        mpg = st.number_input('average mpg - delivery van is 17')
        input_wage = st.number_input('wage')
        input_miles = st.number_input('route miles, round')
        input_time = st.number_input('route time in minutes, round')
        total_stops = st.number_input('route stops')
    calculate = st.form_submit_button('calculate')
    if calculate == True:
        manual(input_wage, input_miles, input_time, total_stops,gas,mpg)

