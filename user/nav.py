# import streamlit as st
# import pymongo

# # Connect to MongoDB
# client = pymongo.MongoClient("mongodb://localhost:27017/?directConnection=true")
# db = client["quiz_db"]
# questions_collection = db["quiz_questions"]
# responses_collection = db["user_responses"]

# # Streamlit app
# st.title("Quiz Web App")

# # Create a list of question numbers
# question_numbers = [1, 2, 3, 4, 5]  # Add more question numbers as needed

# # Create a sidebar navigation bar
# st.sidebar.title("Question Numbers")

# # Add radio buttons for question selection in the sidebar
# selected_question = st.sidebar.radio("Select a Question", question_numbers)

# # Create a set to keep track of solved questions
# solved_questions = set()

# # Define content for each question
# question_content = {
#     1: "This is the content of Question 1.",
#     2: "This is the content of Question 2.",
#     3: "This is the content of Question 3.",
#     4: "This is the content of Question 4.",
#     5: "This is the content of Question 5.",
# }

# # Check if the selected question has been solved
# if selected_question in solved_questions:
#     # Change the color of the selected question number to green if solved
#     st.sidebar.markdown(
#         f'<span style="color: green;">Question {selected_question}</span>',
#         unsafe_allow_html=True
#     )
# else:
#     # Display the selected question number in the default color
#     st.sidebar.markdown(
#         f'Question {selected_question}',
#         unsafe_allow_html=True
#     )

# # Display the selected question's title and content in the main area
# st.subheader(f"Question {selected_question}")
# st.write(question_content[selected_question])

# # Add a button to mark the question as solved
# if st.button("Submit"):
#     solved_questions.add(selected_question)

# # Check if the user has selected a question
# if selected_question:
#     # Function to display and handle the quiz
#     def display_quiz():
#         # Fetch quiz questions from MongoDB
#         questions = list(questions_collection.find())
        
#         # Create a state variable to keep track of the current question index
#         current_question_index = st.session_state.get("current_question_index", 0)

#         # Create a dictionary to store user responses
#         user_responses = st.session_state.get("user_responses", {})

#         if current_question_index < len(questions):
#             question = questions[current_question_index]
#             st.write(question["question"])
#             options = question["options"]
#             selected_option = st.radio("Select an option:", options)
            
#             # Store user response in the dictionary
#             user_responses[question["_id"]] = selected_option

#             # Display the "Next" button
#             if st.button("Next"):
#                 # Increment the question index to move to the next question
#                 current_question_index += 1

#         # Update the state variables
#         st.session_state["current_question_index"] = current_question_index
#         st.session_state["user_responses"] = user_responses

#         # Check if all questions are answered to display the "Submit" button
#         if current_question_index == len(questions):
#             if st.button("Submit"):
#                 # Calculate and display the results
#                 correct_answers = 0
#                 for question in questions:
#                     if user_responses.get(question["_id"]) == question["answer"]:
#                         correct_answers += 1

#                 st.write(f"You answered {correct_answers} out of {len(questions)} questions correctly.")
#                 # You can also store the results in the database if needed.

#     # Run the quiz
#     display_quiz()



import streamlit as st
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/?directConnection=true")
db = client["quiz_db"]
questions_collection = db["quiz_questions"]
responses_collection = db["user_responses"]

# Streamlit app
st.title("Quiz Web App")

# Create a list of question numbers
question_numbers = [1, 2, 3, 4, 5]  # Add more question numbers as needed

# Create a sidebar navigation bar
st.sidebar.title("Question Numbers")

# Add radio buttons for question selection in the sidebar
selected_question = st.sidebar.radio("Select a Question", question_numbers)

# Create a set to keep track of solved questions
solved_questions = set()

# Define content for each question
question_content = {
    1: "This is the content of Question 1.",
    2: "This is the content of Question 2.",
    3: "This is the content of Question 3.",
    4: "This is the content of Question 4.",
    5: "This is the content of Question 5.",
}

# Check if the selected question has been solved
if selected_question in solved_questions:
    # Change the color of the selected question number to green if solved
    st.sidebar.markdown(
        f'<span style="color: green;">Question {selected_question}</span>',
        unsafe_allow_html=True
    )
else:
    # Display the selected question number in the default color
    st.sidebar.markdown(
        f'Question {selected_question}',
        unsafe_allow_html=True
    )

# Function to display the question content based on the selected question
def display_question(selected_question):
    st.subheader(f"Question {selected_question}")
    st.write(question_content[selected_question])

# Display the selected question's title and content in the main area
if selected_question:
    display_question(selected_question)

# Add a button to mark the question as solved
if st.button("Submit"):
    solved_questions.add(selected_question)

# Check if the user has selected a question
if selected_question:
    # Function to display and handle the quiz
    def display_quiz():
        # Fetch quiz questions from MongoDB
        questions = list(questions_collection.find())
        
        # Create a state variable to keep track of the current question index
        current_question_index = st.session_state.get("current_question_index", 0)

        # Create a dictionary to store user responses
        user_responses = st.session_state.get("user_responses", {})

        if current_question_index < len(questions):
            question = questions[current_question_index]
            st.write(question["question"])
            options = question["options"]
            selected_option = st.radio("Select an option:", options)
            
            # Store user response in the dictionary
            user_responses[question["_id"]] = selected_option

            # Display the "Next" button
            if st.button("Next"):
                # Increment the question index to move to the next question
                current_question_index += 1

        # Update the state variables
        st.session_state["current_question_index"] = current_question_index
        st.session_state["user_responses"] = user_responses

        # Check if all questions are answered to display the "Submit" button
        if current_question_index == len(questions):
            if st.button("Submit"):
                # Calculate and display the results
                correct_answers = 0
                for question in questions:
                    if user_responses.get(question["_id"]) == question["answer"]:
                        correct_answers += 1

                st.write(f"You answered {correct_answers} out of {len(questions)} questions correctly.")
                # You can also store the results in the database if needed.

    # Run the quiz
    display_quiz()

