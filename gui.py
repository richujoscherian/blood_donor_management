import streamlit as st

from blood_donor_views import BloodDonorManager

tab1,tab2=st.tabs(["ADD","Show"])
with tab1:
    st.title("add your data")
    name=st.text_input("enter your name")
    blood_group=st.text_input("enter your blood group")
    phone=st.text_input("enter phone number")
    city=st.text_input("enter city")
    last_donation=st.text_input("enter the last donation date")
    if st.button("add new donor")
        donor_instance.post(name=name)
with tab2:
    st.title("shows your data")
