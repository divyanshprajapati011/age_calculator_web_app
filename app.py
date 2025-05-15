import pandas as pd 
import streamlit as st 
from datetime import datetime , timedelta


st.title("Welcome to Age calculator App ")
name = st.text_input("Enter Your Name : ")
dob  = st.date_input("Enter Your D.O.B ", min_value=datetime(1900,1,1).date())
cod = st.date_input(" Todays Date " )

choice = st.selectbox("Enter Your Choice " , ["Day" , "Month ","Year" , "Y/M/D"])
button  = st.button("submit ")

age_day = (cod-dob).days
age_year = (((cod-dob).days)/30)/12
age_month = ((cod-dob).days)/30

if button == True:
    if  choice=="Day":
        st.success(f"thank You... ! {name} you are {int(age_day)} days old ")
    elif choice == "Year":
        st.success(f"thank You... ! {name} you are {int(age_year)} year old ")
    elif choice == "Y/M/D" : 
        year = cod.year - dob.year 
        month = cod.month -  dob.month
        days = cod.day - dob.day
        if days < 0:
            month -= 1
            previous_month = cod.replace(day=1) - timedelta(days=1)
            days += previous_month.day

        if month < 0:
            year -= 1
            month += 12

        st.success(f"thank You... ! {name} you are {int(year)} year {int(month)} month {int(days)} days old ")
    else :
        st.success(f"thank You... ! {name} you are {int(age_month)} month old ")

        

