import pandas as pd 
import streamlit as st 
import datetime


st.title("Welcome to Age calculator App ")
name = st.text_input("Enter Your Name : ")
dob  = st.date_input("Enter Your D.O.B ", min_value=datetime.date(1900,1,1))
cod = st.date_input(" Todays Date ")

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
    elif choice == "Month" :
        st.success(f"thank You... ! {name} you are {int(age_month)} month old ")
    else : 
        year = age_year
        month = ((dob.month)-(cod.month))
        days = ((cod.day)-(dob.day))
        st.success(f"thank You... ! {name} you are {int(year)} year {int(month)} month {int(days)} days old ")


        

