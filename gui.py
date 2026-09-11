import streamlit as st

from blood_donor_views import BloodDonorManager
donor_instance = BloodDonorManager()
tab1,tab2=st.tabs(["ADD","Show"])
with tab1:
    st.title("add your data")
    name=st.text_input("enter your name")
    blood_group=st.selectbox("enter your blood group",[" ","A+","B+","A-","B-","AB-","AB+","O+","O-"])
    phone=st.text_input("enter phone number")
    city=st.text_input("enter city")
    last_donation=st.text_input("enter the last donation date")

    if st.button("add new donor"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("added succesfully")
with tab2:
    st.title("shows your data")
    records=donor_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("no data found")

