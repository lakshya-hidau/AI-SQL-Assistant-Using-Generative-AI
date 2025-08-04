# 🧑‍💻 AI SQL Assistant

Welcome to **AI SQL Assistant** – an interactive Streamlit app that lets you query your database using natural language! Powered by Google Gemini and SQLite, this tool converts your English questions into SQL queries, executes them, and displays the results instantly.

![AI SQL Assistant Banner](https://img.shields.io/badge/AI-SQL-blueviolet?style=for-the-badge)

**Live Link** - (https://ai-sql-assistant-using-generative-ai.streamlit.app/)
---

## 🚀 Features

- **Natural Language to SQL**: Ask questions in plain English and get the corresponding SQL query.
- **Instant Results**: Executes the generated SQL on your local SQLite database and shows results in a table.
- **Google Gemini Integration**: Uses Google Generative AI for accurate SQL generation.
- **User-Friendly UI**: Clean, interactive interface built with Streamlit.

---

## 🏗️ Project Structure

```
.
├── app.py
├── student.db
├── .env
├── requirements.txt
└── ...
```

---

## ⚡ Getting Started

1. **Clone the repository**
    ```sh
    git clone https://github.com/lakshya-hidau/AI-SQL-Assistant-Using-Generative-AI
    cd <project-directory>
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up your environment**
    - Create a `.env` file with your Google API key:
        ```
        GOOGLE_API_KEY=your-google-api-key
        ```

4. **Run the app**
    ```sh
    streamlit run app.py
    ```

---

## 🗃️ Database Schema

The app expects a SQLite database named `student.db` with a table called `STUDENT`:

| NAME | CLASS | SECTION | MARKS |
|------|-------|---------|-------|

---

## 💡 Example Questions

- *How many students are in AI+DS?*
- *List all students in class 10.*
- *How many entries are there in the table?*

---

## 🛡️ Disclaimer

- The AI-generated SQL is only as accurate as the model and prompt allow. Always review queries before running on production data.
- This project is for educational/demo purposes.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

Enjoy querying your database the smart
