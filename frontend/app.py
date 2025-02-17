import streamlit as st
import requests

# API Endpoints
API_URL_CHAT = "http://127.0.0.1:8000/chat"
API_URL_CALL_ME = "http://127.0.0.1:8000/call_me"
API_URL_BOOK_APPOINTMENT = "http://127.0.0.1:8000/book_appointment"

st.title("Chatbot")

user_input = st.text_input("Ask something:")

if user_input.lower() == "call me":
    st.subheader("Enter Your Details for a Call:")
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")

    if st.button("Request a Call"):
        if name and email and phone:
            try:
                response = requests.post(API_URL_CALL_ME, json={"name": name, "email": email, "phone": phone})
                if response.status_code == 200:
                    st.write(response.json().get("response", "No response found"))
                else:
                    st.write(f"Error: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.write(f"Request failed: {e}")
        else:
            st.write("Please fill in all details.")

elif user_input.lower() == "book appointment":
    st.subheader("Enter Your Details for Appointment:")
    name = st.text_input("Name:")
    email = st.text_input("Email:")
    phone = st.text_input("Phone:")
    appointment_date = st.date_input("Select Appointment Date:")

    if st.button("Book Appointment"):
        if name and email and phone and appointment_date:
            try:
                response = requests.post(API_URL_BOOK_APPOINTMENT, json={
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "date": str(appointment_date)
                })
                if response.status_code == 200:
                    st.write(response.json().get("response", "No response found"))
                else:
                    st.write(f"Error: {response.status_code}")
            except requests.exceptions.RequestException as e:
                st.write(f"Request failed: {e}")
        else:
            st.write("Please fill in all details.")

elif st.button("Send"):
    if user_input:
        try:
            response = requests.post(API_URL_CHAT, json={"query": user_input})
            if response.status_code == 200:
                st.write(response.json().get("response", "No response found"))
            else:
                st.write(f"Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.write(f"Request failed: {e}")
