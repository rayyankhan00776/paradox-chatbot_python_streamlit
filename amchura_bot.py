import streamlit as st
import google.generativeai as genai
import time

# Configure the API key

api_key = "AIzaSyAGYjDFLBmZZi7h_JA5Mbu6m6Qj7C_y-bE"
genai.configure(api_key=api_key)

# Set the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get response from the model
def getresponse(userinput):
    response = model.generate_content(userinput)
    return response.text

# Streamlit App Layout
st.title("paradox Bot with Masala Response")
st.subheader("Generates a masala-flavored response to your query")

# Add an image at the top (you can replace the link with your image URL or local image)
st.image("images.jpg", use_column_width=True)

# Input field with placeholder text
userinput = st.text_input("Bolo bhai / bhen :", placeholder="Ask your question with a sprinkle of masala...")

# Button to generate response
if st.button("Generate Response"):
    if userinput:
        with st.spinner('Cooking up your masala response...'):
            time.sleep(2)  # Simulate a delay to make the app feel more responsive
        output = getresponse(userinput)
        st.write(f"**Response:** {output}")
    else:
        st.warning("Please enter some input.")

# Footer section with contact details or credits
st.write("---")
st.write("Made with ❤️ by Rayonix Solutions")
