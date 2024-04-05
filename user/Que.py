import streamlit as st
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["quiz_db"]
questions_collection = db["quiz_questions"]
responses_collection = db["user_responses"]

# Streamlit app
st.title("Quiz Web App")

# Function to display and handle the quiz
def display_quiz():
    # Fetch quiz questions from MongoDB
    questions = list(questions_collection.find())
    
    # Loop through questions and display them to the user
    for question in questions:
        st.write(question["question"])
        options = question["options"]
        selected_option = st.radio("Select an option:", options)
        
        # Store user response in MongoDB
        user_response = {"question_id": question["_id"], "response": selected_option}
        responses_collection.insert_one(user_response)

# Display the quiz to the user
display_quiz()
