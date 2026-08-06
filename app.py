import streamlit as st
import requests

st.title("Sleep Quality Dashboard")

reading_id = st.number_input("Reading ID", min_value=1, step=1)

if st.button("Get Reading"):
    response = requests.get(f"http://localhost:8000/readings/{reading_id}")
    if response.status_code == 200:
        data = response.json()
        st.write(data)
        st.metric("Heart Rate", data["heart_rate"])
    else:
        st.error("Reading not found")
