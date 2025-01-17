import streamlit as st
import os
import pandas as pd

# Function to load file and return a set of errors
def load_file(file):
    return set(line.strip() for line in file)

# Function to process uploaded files and return unique errors
def process_files(uploaded_files):
    errors = set()
    errorcount = 0
    file_errors = {}  # Dictionary to hold unique errors for each file

    for uploaded_file in uploaded_files:
        # Read the file content
        error_logs = load_file(uploaded_file)
        
        # Get unique errors by finding the difference
        unique_errors = error_logs - errors
        errors.update(unique_errors)
        errorcount += len(unique_errors)

        # Store unique errors for the current file
        file_errors[uploaded_file.name] = unique_errors
    
    return errors, errorcount, file_errors  # Return the file_errors dictionary

# Streamlit interface
st.title("Unique Error Logs Extractor")

st.write("Upload your error log files, and this tool will extract unique errors and allow you to download them.")

# File uploader
uploaded_files = st.file_uploader("Choose error log files", accept_multiple_files=True)

if uploaded_files:
    # Process the files to get unique errors
    errors, errorcount, file_errors = process_files(uploaded_files)

    # Show the result
    st.write(f"Total unique errors found: {errorcount} across {len(file_errors)} files.")
    
    # Convert the set to a sorted list before displaying it
    sorted_errors = sorted(errors)

    # Display a table with unique errors in rows and file names in columns
    st.write("Unique Errors by File:")
    unique_errors_table = {file_name: list(errors) for file_name, errors in file_errors.items()}
    

    # Button to download the unique errors as a text file
    if st.button('Download Unique Errors'):
        # Create a text file with the desired format
        with open("unique_errors_table.txt", "w") as f:  # Open the file for writing
            for file_name, errors in unique_errors_table.items():
                f.write(f"{file_name}\n")  # Write the filename
                for error in errors:
                    f.write(f"{error.decode('utf-8')}\n")  # Decode each byte string to a regular string
                f.write("\n")  # Add a newline for separation between files
else:
    st.write("Please upload some error log files to proceed.")
