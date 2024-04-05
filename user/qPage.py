import streamlit as st
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["quiz_pass"]
collection = db["password"]

st.title("Login page")
username = st.text_input("Enter your name")
password = st.text_input("Password:", type="password")

if username and password:
    # Create a document and insert it into the MongoDB collection
    user_document = {
        "username": username,
        "password": password
    }
    
    result = collection.insert_one(user_document)
    st.info(f"Document inserted with ObjectID: {result.inserted_id}")

    st.success("Data has been automatically stored in the database.")
    
correct_username = "username"
correct_password = "password"

if st.button("Login"):
    if username == correct_username and password == correct_password:
        st.success("Logged in as: " + username)
    else:
        st.error("Incorrect username or password. Please try again.")
