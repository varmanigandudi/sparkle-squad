import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDYBfT_K1eOq6034Oa2x5-0UFr0Rz1r7yc")  # Replace with your API key

# Set up the Streamlit app
st.title("AI-Powered Personalized Email Generator")

# Input fields for email details
recipient = st.text_input("Recipient Name")
sender = st.text_input("Sender Name")
subject = st.text_input("Subject")
context = st.text_area("Email Context")

# Button to generate email
if st.button("Generate Email"):
    if recipient and sender and subject and context:
        # Construct the prompt for Gemini AI
        prompt = f"Generate a personalized email from {sender} to {recipient} with the subject '{subject}'. The email should be about: {context}"

        # Call the Gemini API to generate the email content
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            st.subheader("Generated Email:")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.error("Please fill in all fields.")