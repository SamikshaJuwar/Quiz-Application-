import streamlit as st
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://your_username:your_password@your_mongodb_host:your_mongodb_port/")
db = client["your_database_name"]
collection = db["your_collection_name"]

st.title("Login page")
username = st.text_input("Enter your name")
password = st.text_input("Password:", type="password")

correct_username = "username"
correct_password = "password"

if st.button("Login"):
    if username == correct_username and password == correct_password:
        st.success("Logged in as: " + username)
        
        # Create a document and insert it into the MongoDB collection
        user_document = {
            "username": username,
            "password": password
        }
        
        result = collection.insert_one(user_document)
        st.info(f"Document inserted with ObjectID: {result.inserted_id}")
        
    else:
        st.error("Incorrect username or password. Please try again.")
