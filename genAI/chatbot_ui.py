import streamlit as st
from  chatbot.chatbot import handle_user_query, update_user_status


def ChatBotApp():
    # Streamlit UI
    st.title("Recruitment Chatbot")

    # Simulate user login (for demonstration)
    user_id = st.text_input("Enter your User ID:")

    if user_id:
        user_query = st.text_input("Ask a question about the job or application status:")

        if user_query:
            # Process user query
            response = handle_user_query(user_id, user_query)
            st.write(response)

        # # Option to update application status
        # new_status = st.selectbox(
        #     "Update your application status:",
        #     ["Applied", "Under Review", "Interview Scheduled", "Rejected", "Accepted"]
        # )

        # if st.button("Update Status"):
        #     status_response = update_user_status(user_id, new_status)
        #     st.write(status_response)
    else:
        st.write("Please enter your User ID to continue.")
