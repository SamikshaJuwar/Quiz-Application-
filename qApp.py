# import streamlit as st
# import pymongo
# import random
# from PIL import Image


# image = Image.open('D:\QuizProject\quiz.jpg')
# st.image(image, caption='  ')


# # Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/?directConnection=true")
# db = client["quiz_db"]
# questions_collection = db["quiz_questions"]
# responses_collection = db["user_responses"]

# # Streamlit app
# st.title("Quiz Web App")

# # Function to fetch random questions with a maximum of 25 questions
# def get_random_questions(num_questions):
#     all_questions = list(questions_collection.find())
#     random.shuffle(all_questions)
#     return all_questions[:min(num_questions, 25)]


# # Function to collect user information on the first page
# def user_info_page():
#     mongo_client = pymongo.MongoClient("mongodb://localhost:27017/?directConnection=true")
#     db = mongo_client["quiz_db"]
#     collection = db["user_info"]

#     username = st.text_input("Enter your name:")
#     password = st.text_input("Password:", type="password")
#     email = st.text_input("Enter your email:")
#     course = st.selectbox("Enter your course:", ("Python", "Data Science", "Artificial Intelligence", "Machine Learning", "Java", "Full Stack Development"))
#     date = st.date_input("Enter Date:")
#     gender_options = ["Male", "Female", "Other"]
#     gender = st.radio("Select your gender:", gender_options)

#     st.divider()

#     if st.button("Start Quiz"):
#     # Convert the date to a string before saving to MongoDB
#          date_str = date.strftime("%Y-%m-%d")

#     # Create a dictionary with user data
#          user_data = {
#              "username": username,
#              "password": password,
#              "email": email,
#              "course": course,
#              "date": date_str,  # Convert date to string
#              "gender": gender
#     }

#     # Insert the user data into the MongoDB collection
#     collection.insert_one(user_data)

#     if st.button("Start Quiz"):
#         if username == username and password == password:
#             st.success("Logged in as: " + username)
#     else:
#         st.error("Incorrect username or password. Please try again.")

# # Close the MongoDB client connection when your Streamlit app is done
#     mongo_client.close()


# # Function to display and handle the quiz on the second page
# def quiz_page(user_info):
#     st.subheader("Quiz")
    
#     num_questions = 25  # Maximum of 25 questions
#     questions = get_random_questions(num_questions)
#     current_question_index = st.session_state.get("current_question_index", 0)
#     user_responses = st.session_state.get("user_responses", {})

#     if current_question_index < len(questions):
#         question = questions[current_question_index]
#         st.write(f"Question {current_question_index + 1}: {question['question']}")  # Add question number
#         options = question["options"]
#         selected_option = st.radio("Select an option:", options)
#         user_responses[question["_id"]] = selected_option

#         if st.button("Next"):
#             current_question_index += 1

#     st.session_state["current_question_index"] = current_question_index
#     st.session_state["user_responses"] = user_responses

#     if current_question_index == len(questions):
#         if st.button("Submit"):
#             correct_answers = 0
#             for question in questions:
#                 if user_responses.get(question["_id"]) == question["answer"]:
#                     correct_answers += 1

#             st.write(f"You answered {correct_answers} out of {len(questions)} questions correctly.")
        

# # Check if the quiz has started
# if "quiz_started" not in st.session_state or not st.session_state["quiz_started"]:
#     user_info_page()
# else:
#     user_info = st.session_state["user_info"]
#     quiz_page(user_info)





# import streamlit as st
# import pymongo
# from PIL import Image

# # Connect to MongoDB
# mongo_client = pymongo.MongoClient("mongodb://localhost:27017/?directConnection=true")
# db = mongo_client["quiz_db"]
# questions_collection = db["quiz_questions"]
# responses_collection = db["user_responses"]
# user_info_collection = db["user_info"]

# # Load the image
# image = Image.open('D:\QuizProject\quiz.jpg')
# st.image(image, caption='Quiz')

# # Streamlit app
# st.title("Quiz Web App")

# # Function to collect user information on the first page
# def user_info_page():
#     username = st.text_input("Enter your name:")
#     password = st.text_input("Password:", type="password")
#     email = st.text_input("Enter your email:")
#     course = st.selectbox("Enter your course:", ("Python", "Data Science", "Artificial Intelligence", "Machine Learning", "Java", "Full Stack Development"))
#     date = st.date_input("Enter Date:")
#     gender_options = ["Male", "Female", "Other"]
#     gender = st.radio("Select your gender:", gender_options)

#     st.divider()

#     if st.button("Start Quiz"):
#         # Check if user info is valid and not empty
#         if not (username and password and email and course and date and gender):
#             st.error("Please fill in all the fields.")
#         else:
#             # Convert the date to a string before saving to MongoDB
#             date_str = date.strftime("%Y-%m-%d")

#             # Create a dictionary with user data
#             user_data = {
#                 "username": username,
#                 "password": password,  # In a real app, hash the password securely
#                 "email": email,
#                 "course": course,
#                 "date": date_str,  # Convert date to string
#                 "gender": gender
#             }

#             # Insert the user data into the MongoDB collection
#             user_info_collection.insert_one(user_data)
            
#             st.success("Registration successful. You can now start the quiz.")

# # Function to display and handle the quiz on the second page
# def quiz_page():
#     st.subheader("Quiz")
    
#     num_questions = 25  # Maximum of 25 questions
#     questions = get_random_questions(num_questions)
#     current_question_index = st.session_state.get("current_question_index", 0)
#     user_responses = st.session_state.get("user_responses", {})

#     if current_question_index < len(questions):
#         question = questions[current_question_index]
#         st.write(f"Question {current_question_index + 1}: {question['question']}")  # Add question number
#         options = question["options"]
#         selected_option = st.radio("Select an option:", options)
#         user_responses[question["_id"]] = selected_option

#         if st.button("Next"):
#             current_question_index += 1

#     st.session_state["current_question_index"] = current_question_index
#     st.session_state["user_responses"] = user_responses

#     if current_question_index == len(questions):
#         if st.button("Submit"):
#             correct_answers = 0
#             for question in questions:
#                 if user_responses.get(question["_id"]) == question["answer"]:
#                     correct_answers += 1

#             st.write(f"You answered {correct_answers} out of {len(questions)} questions correctly.")

# # Function to fetch random questions with a maximum of 25 questions
# def get_random_questions(num_questions):
#     all_questions = list(questions_collection.find())
#     random.shuffle(all_questions)
#     return all_questions[:min(num_questions, 25)]

# # Check if the quiz has started
# if "quiz_started" not in st.session_state or not st.session_state["quiz_started"]:
#     user_info_page()
#     st.session_state["quiz_started"] = True  # Mark the quiz as started
# else:
#     quiz_page()

# # Close the MongoDB client connection when your Streamlit app is done
# mongo_client.close()





import streamlit as st
import pymongo
import random

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["quiz_db"]

# Define the collection for user data
users_collection = db["users"]

# Function to fetch random questions for the selected course
def get_random_questions(num_questions, selected_course):
    course_collection = db[f"{selected_course.lower()}_datascience_questions"]
    all_questions = list(course_collection.find())
    random.shuffle(all_questions)
    return all_questions[:min(num_questions, 60)]

# Initialize session state
if "registration_completed" not in st.session_state:
    st.session_state.registration_completed = False
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "user_info" not in st.session_state:
    st.session_state.user_info = None

# Function to collect user information on the registration page
def registration_page():
    st.subheader("User Registration")

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

    user_info = {
        "username": username,
        "password": password,
        "email": email,
        "course": course,
        "gender": gender,
    }

    if st.button("Register"):
        users_collection.insert_one(user_info)
        st.session_state.user_info = user_info
        st.session_state.registration_completed = True
        st.session_state.quiz_started = True

# Function to display and handle the quiz on the next page
def quiz_page(user_info):
    st.subheader("Quiz")
    num_questions = 60

    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = get_random_questions(num_questions, user_info["course"])
        st.session_state.current_question_index = 0
        st.session_state.user_responses = {}

    current_question_index = st.session_state.current_question_index
    questions = st.session_state.quiz_questions
    user_responses = st.session_state.user_responses

    if current_question_index < len(questions):
        question = questions[current_question_index]
        st.write(f"Question {current_question_index + 1}: {question['question']}")

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

# Main logic
if not st.session_state.registration_completed:
    registration_page()
elif not st.session_state.quiz_started:
    st.write("Registration completed. Click the button below to start the quiz.")
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
else:
    user_info = st.session_state.user_info
    quiz_page(user_info)
