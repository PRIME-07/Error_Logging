# Unique Error Logs Script

This is a script to extract and save only the **unique error logs** from multiple files.

## Prerequisites
Before running the script, ensure you have all the necessary dependencies installed.

### Installation
Install the required packages by running the following command:
```bash
pip install -r requirements.txt
```

### Usage
To run the script, execute the following command:
```bash
streamlit run unique_logs.py
```
This will launch a Streamlit interface where you can:

- Upload multiple error log files.
- Extract and combine unique errors from all files.
- Download the consolidated file containing only the unique errors.

### Output
The output will be available as a downloadable .txt file.