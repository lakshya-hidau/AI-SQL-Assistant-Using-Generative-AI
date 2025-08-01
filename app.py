from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

import streamlit as st
import google.generativeai as genai
import os
import sqlite3
import pandas as pd

# Set up the Google Generative AI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

# Function to retrieve query from database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        rows = cursor.fetchall()
        return columns, rows, None
    except Exception as e:
        return [], [], str(e)
    finally:
        connection.close()

# Define your prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries.
    The SQL database has the name STUDENT and has the following columns:
    NAME, CLASS, SECTION.
    For example,\nExample 1 - How many entries of records are there in the table?,
    the SQL command will be something like:
    SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - How many students studied in AI+DS?,
    the SQL command will be something like:
    SELECT * FROM STUDENT WHERE SECTION = 'AI+DS'; 
    also the sql code should not have ``` in begining or end and sql word in output.
    """
]

# Streamlit app layout
st.set_page_config(page_title="SQL Query Generator", page_icon=":guardsman:", layout="centered")
st.title("🔎 Natural Language to SQL Query Generator")
st.markdown(
    """
    Enter your question in plain English and let AI generate the SQL query and fetch results from your database!
    """
)

with st.form("query_form"):
    question = st.text_input(
        "Ask a question about your STUDENT database:",
        placeholder="e.g., How many students are in AI+DS?",
        key="input"
    )
    submitted = st.form_submit_button("Generate & Run Query")

if submitted and question.strip():
    with st.spinner("Generating SQL query..."):
        sql_query = get_gemini_response(question, prompt)
    st.markdown("#### Generated SQL Query")
    st.code(sql_query, language="sql")

    with st.spinner("Running query on database..."):
        columns, rows, error = read_sql_query(sql_query, 'student.db')

    if error:
        st.error(f"Error executing SQL: {error}")
    elif rows:
        st.markdown("#### Query Results")
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No results found for your query.")
else:
    st.info("Enter a question and click 'Generate & Run Query' to get started.")