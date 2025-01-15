import streamlit as st
import os

# Function to load file and return a set of errors
def load_file(file):
    return set(line.strip() for line in file)

# Function to process uploaded files and return unique errors
def process_files(uploaded_files):
    errors = set()
    errorcount = 0

    for uploaded_file in uploaded_files:
        # Read the file content
        error_logs = load_file(uploaded_file)
        
        # Get unique errors by finding the difference
        unique_errors = error_logs - errors
        errors.update(unique_errors)
        errorcount += len(unique_errors)
    
    return errors, errorcount

# Streamlit interface
st.title("Unique Error Logs Extractor")

st.write("Upload your error log files, and this tool will extract unique errors and allow you to download them.")

# File uploader
uploaded_files = st.file_uploader("Choose error log files", accept_multiple_files=True)

if uploaded_files:
    # Process the files to get unique errors
    errors, errorcount = process_files(uploaded_files)

    # Show the result
    st.write(f"Total unique errors found: {errorcount}")
    
    # Convert the set to a sorted list before displaying it
    sorted_errors = sorted(errors)

    # Ensure all items are strings before joining (decode if bytes)
    sorted_errors_str = [error.decode('utf-8') if isinstance(error, bytes) else str(error) for error in sorted_errors]

    # Display the unique errors in the text area
    st.text_area("Unique Errors", "\n".join(sorted_errors_str), height=300)

    # Button to download the unique errors as a text file
    if st.button('Download Unique Errors'):
        with open("unique_errors.txt", "w") as f:
            for error in sorted_errors_str:
                f.write(error + "\n")
        
        # Provide download link for the unique errors file
        with open("unique_errors.txt", "rb") as f:
            st.download_button(
                label="Download unique_errors.txt",
                data=f,
                file_name="unique_errors.txt",
                mime="text/plain"
            )
else:
    st.write("Please upload some error log files to proceed.")
