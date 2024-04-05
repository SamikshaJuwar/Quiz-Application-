import streamlit as st
import pymongo
import random

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["quiz_db"]
user_responses = db["user_responses"]


# Define the collection for user data
users_collection = db["users"]
# Function to fetch random questions for the selected course
def get_random_questions(num_questions, selected_course):
    # Specify the collection based on the selected course
    course_collection = db[f"{selected_course.lower()}_questions"]

    all_questions = list(course_collection.find())
    random.shuffle(all_questions)
    return all_questions[:min(num_questions, 25)]

# Function to collect user information on the registration page
def registration_page():
    st.subheader("User Registration")

    # Collect user registration information
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    course_options = [
        "Python",
        "Data_Science",
        "Machine_Learning",
        "Java",
        "C++",
        "C"
    ]
    course = st.selectbox("Choose your course:", course_options)
    gender = st.radio("Gender", ["Male", "Female", "Other"])

    # Store user registration information in a dictionary
    user_info = {
        "username": username,
        "password": password,
        "email": email,
        "course": course,
        "gender": gender,
    }

    if st.button("Register"):
        # Insert user information into the database
        users_collection.insert_one(user_info)
        st.session_state["user_info"] = user_info
        st.session_state["quiz_started"] = True
        st.session_state["registration_completed"] = True

# Function to display and handle the quiz on the next page
def quiz_page(user_info):
    st.subheader("Quiz")

    num_questions = 25  # Maximum of 25 questions

    # Retrieve or initialize the questions in session state
    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = get_random_questions(num_questions, user_info["course"])
        st.session_state.current_question_index = 0
        st.session_state.user_responses = {}

    current_question_index = st.session_state.current_question_index
    questions = st.session_state.quiz_questions
    user_responses = st.session_state.user_responses

    if current_question_index < len(questions):
        question = questions[current_question_index]
        st.write(f"Question {current_question_index + 1}: {question['question']}")  # Add question number

        # Initialize selected_option to None
        

        # Use radio buttons for options, which will initially have no option selected
        selected_option = st.radio("Select an option:", question["options"], key=f"question_{current_question_index}")
        user_responses[question["_id"]] = selected_option

        if current_question_index < len(questions) - 1:
            if st.button("Next"):
                current_question_index += 1
                st.session_state.current_question_index = current_question_index
        else:
            if st.button("Submit"):
                correct_answers = 0
                for question in questions:
                    if user_responses.get(question["_id"]) == question["answer"]:
                        correct_answers += 1

                st.write(f"You answered {correct_answers} out of {len(questions)} questions correctly.")

# Check if the quiz should start
if "registration_completed" not in st.session_state or not st.session_state["registration_completed"]:
    registration_page()
elif "quiz_started" not in st.session_state or not st.session_state["quiz_started"]:
    st.write("Registration completed. Click the button below to start the quiz.")
    if st.button("Start Quiz"):
        st.session_state["quiz_started"] = True
else:
    user_info = st.session_state["user_info"]
    quiz_page(user_info)
    