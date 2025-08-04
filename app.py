from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

import streamlit as st
import google.generativeai as genai
import os
import sqlite3
import pandas as pd
import tempfile

# Set up the Google Generative AI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

# Function to retrieve query from database
def read_sql_query(sql, db_path):
    connection = sqlite3.connect(db_path)
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

# Define prompt for Gemini
prompt = [
    """
    You are an expert in converting English questions to SQL queries.
    The SQL database has the name STUDENT and has the following columns:
    NAME, CLASS, SECTION.
    For example,
    Example 1 - How many entries of records are there in the table?
    SELECT COUNT(*) FROM STUDENT;
    Example 2 - How many students studied in AI+DS?
    SELECT * FROM STUDENT WHERE SECTION = 'AI+DS'; 
    Avoid using triple backticks (```) or the word "sql" in output.
    """
]

# Streamlit App UI
st.set_page_config(page_title="SQL Query Generator", page_icon=":guardsman:", layout="centered")
st.title("🧠 Natural Language to SQL Query Generator")

st.markdown("""
Ask any question about your **STUDENT** database and get instant SQL + query results!

**Choose your data source below:**
""")

# Select DB Mode
db_mode = st.radio("Database Source:", ("Use Demo DB (student.db)", "Upload Your Own DB"))

# Handle DB upload
uploaded_db_path = None
if db_mode == "Upload Your Own DB":
    uploaded_file = st.file_uploader("Upload your SQLite `.db` file", type=["db", "sqlite"])
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp:
            tmp.write(uploaded_file.read())
            uploaded_db_path = tmp.name

# Input form
with st.form("query_form"):
    question = st.text_input(
        "Ask a question:",
        placeholder="e.g., How many students are in AI+DS?",
        key="input"
    )
    submitted = st.form_submit_button("Generate & Run Query")

if submitted:
    if not question.strip():
        st.warning("Please enter a question.")
    elif db_mode == "Upload Your Own DB" and uploaded_db_path is None:
        st.warning("Please upload a valid `.db` file.")
    else:
        db_path = uploaded_db_path if uploaded_db_path else "student.db"

        with st.spinner("Generating SQL query using Gemini..."):
            sql_query = get_gemini_response(question, prompt)

        st.markdown("#### 🧾 Generated SQL Query")
        st.code(sql_query, language="sql")

        with st.spinner("Executing query on database..."):
            columns, rows, error = read_sql_query(sql_query, db_path)

        if error:
            st.error(f"❌ Error executing SQL: {error}")
        elif rows:
            st.markdown("#### ✅ Query Results")
            df = pd.DataFrame(rows, columns=columns)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No results found for your query.")
