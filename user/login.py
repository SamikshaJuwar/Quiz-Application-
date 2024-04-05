# import streamlit as st
# username = st.text_input("Enter your name : ")
# email = st.text_input("Enter your mail : ")
# course = st.selectbox("Enter your course : ",("Python","Data science","Artificial Intelligence","machine learning","java","Full Stack Development"))
# date = st.date_input("Enter Date : ")
# gender = st.radio("Gender :",["male","Female","Other"])


# st.divider()

# st.button(":blue[Start Quiz]")



import streamlit as st
import pymongo
from datetime import datetime
from PIL import Image


image = Image.open('D:\QuizProject\quiz.jpg')
st.image(image, caption='  ')


# Connect to MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/?directConnection=true")
db = mongo_client["quiz_pass"]
collection = db["password"]

username = st.text_input("Enter your name:")
password = st.text_input("Password:", type="password")
email = st.text_input("Enter your email:")
course = st.selectbox("Enter your course:", ("Python", "Data Science", "Artificial Intelligence", "Machine Learning", "Java", "Full Stack Development"))
date = st.date_input("Enter Date:")
gender_options = ["Male", "Female", "Other"]
gender = st.radio("Select your gender:", gender_options)

st.divider()

if st.button("Start Quiz"):
    # Convert the date to a string before saving to MongoDB
    date_str = date.strftime("%Y-%m-%d")

    # Create a dictionary with user data
    user_data = {
        "username": username,
        "password": password,
        "email": email,
        "course": course,
        "date": date_str,  # Convert date to string
        "gender": gender
    }

    # Insert the user data into the MongoDB collection
    collection.insert_one(user_data)

    if st.button("Start Quiz"):
        if username == username and password == password:
            st.success("Logged in as: " + username)
    else:
        st.error("Incorrect username or password. Please try again.")

# Close the MongoDB client connection when your Streamlit app is done
mongo_client.close()
