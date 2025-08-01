import sqlite3
import os

# Show path for clarity
print("Using database at:", os.path.abspath("student.db"))

# SQLite database connection
connection = sqlite3.connect('student.db')
cursor = connection.cursor()

# Drop existing table if it exists
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create the table
cursor.execute("""
CREATE TABLE STUDENT (
    NAME VARCHAR(25) NOT NULL,
    CLASS VARCHAR(20),
    SECTION VARCHAR(20),
    MARKS INTEGER DEFAULT 0
);
""")

# Insert data into the table
students = [
    ('Lakshya', 'AI', 'AI+DS', 85),
    ('Anshika', 'AI', 'AI+DS', 90),
    ('Piyush', 'AI', 'AI-A', 75),
    ('Aarav', 'AI', 'DS', 80),
    ('Aarvi', 'AI', 'AI+DS', 88),
    ('Ankit', 'CS', 'C', 95),
    ('Deepak', 'CS', 'E', 92),
    ('Rohit', 'CS', 'C', 78),
    ('Sarvesh', 'CS', 'P', 82),
    ('Aarav Mehra', '10', 'A', 87),
    ('Vihaan Sharma', '9', 'B', 74),
    ('Vivaan Patel', '8', 'C', 65),
    ('Aditya Rao', '10', 'A', 93),
    ('Arjun Nair', '9', 'A', 80),
    ('Reyansh Iyer', '10', 'B', 77),
    ('Krishna Reddy', '8', 'B', 88),
    ('Sai Verma', '7', 'A', 92),
    ('Ishaan Gupta', '9', 'C', 71),
    ('Om Jha', '10', 'C', 85),
    ('Ayaan Das', '7', 'B', 89),
    ('Rudra Singh', '8', 'C', 78),
    ('Kabir Bose', '10', 'A', 81),
    ('Anaya Mishra', '9', 'B', 90),
    ('Myra Kapoor', '8', 'A', 76),
    ('Diya Sen', '10', 'C', 84),
    ('Aadhya Jain', '9', 'A', 73),
    ('Kiara Joshi', '7', 'C', 88),
    ('Saanvi Bhat', '8', 'B', 66),
    ('Anika Roy', '10', 'B', 91),
    ('Navya Sinha', '9', 'A', 79),
    ('Ira Tripathi', '8', 'C', 82),
    ('Meera Yadav', '10', 'A', 86),
    ('Tanya Chatterjee', '7', 'A', 69),
    ('Aarohi Kumar', '9', 'C', 75),
    ('Prisha Thakur', '10', 'B', 94),
    ('Riya Aggarwal', '8', 'A', 83),
    ('Tanvi Bhatt', '9', 'B', 87),
    ('Harsh Patel', '7', 'B', 74),
    ('Raj Aryan', '10', 'C', 78),
    ('Manav Dubey', '8', 'C', 66),
    ('Devansh Malhotra', '9', 'A', 72),
    ('Kunal Saxena', '10', 'B', 88),
    ('Parth Tiwari', '7', 'C', 67),
    ('Yash Mittal', '8', 'A', 70),
    ('Raghav Kohli', '9', 'B', 91),
    ('Neel Vyas', '10', 'A', 77),
    ('Laksh Kapoor', '9', 'C', 86),
    ('Shreyas Desai', '8', 'B', 82),
    ('Shaurya Naik', '7', 'A', 79),
    ('Aman Shetty', '10', 'C', 73),
    ('Aaliya Khan', '8', 'C', 85),
    ('Zara Hussain', '9', 'A', 84),
    ('Jhanvi Farooq', '7', 'B', 80),
    ('Simran Zaveri', '10', 'A', 92),
    ('Sneha D Souza', '9', 'B', 74),
    ('Nitya Salvi', '8', 'A', 68),
    ('Ishita Joshi', '10', 'B', 89),
    ('Kavya Kale', '7', 'C', 83),
    ('Pihu Chavan', '9', 'C', 90),
    ('Sia Kadam', '8', 'B', 76),
    ('Arya Gokhale', '10', 'C', 70),
    ('Dhruv Menon', '9', 'A', 71),
    ('Advait Prabhu', '8', 'C', 87),
    ('Vedant Kamble', '7', 'A', 72),
    ('Tanish Vora', '10', 'B', 95),
    ('Hridaan Thakkar', '9', 'B', 81),
    ('Arnav Rathore', '10', 'A', 85),
    ('Tejas Bhonsle', '8', 'A', 77),
    ('Nirvaan Rajput', '7', 'C', 79),
    ('Aryan Barot', '9', 'C', 82),
    ('Samar Kulkarni', '8', 'B', 69),
    ('Rehaan Saluja', '10', 'C', 80),
    ('Avi Shah', '9', 'A', 75),
    ('Ritvik Khatri', '7', 'B', 73),
    ('Eshan Gaur', '10', 'A', 91),
    ('Pranav Nagar', '8', 'C', 68),
    ('Siddharth Chaudhary', '9', 'B', 84),
    ('Naman Rawal', '7', 'A', 76),
    ('Jay Mehta', '10', 'B', 87),
    ('Divyansh Pandey', '8', 'A', 70),
    ('Utkarsh Jain', '9', 'C', 66),
    ('Anshul Sethi', '7', 'C', 74),
    ('Anirudh Solanki', '10', 'C', 89),
    ('Abhinav Bhagat', '8', 'B', 81),
    ('Chinmay Barua', '9', 'A', 77),
    ('Aaryan Talwar', '10', 'A', 93),
    ('Omkar Hegde', '7', 'B', 67),
    ('Rishabh Khanna', '8', 'A', 75),
    ('Nikhil Suri', '9', 'B', 88),
    ('Deepanshu Gill', '10', 'B', 90),
    ('Saurav Wadhwa', '8', 'C', 78),
    ('Ravindra Bansal', '7', 'A', 71),
    ('Aniket Chauhan', '9', 'C', 72),
    ('Madhav Sengar', '10', 'C', 86),
    ('Vikram Purohit', '8', 'B', 84),
    ('Bhuvan Rana', '9', 'A', 79),
    ('Shivank Rawat', '10', 'B', 74),
    ('Avni Rathi', '7', 'C', 80),
    ('Palak Saxena', '9', 'B', 85),
    ('Niharika Lohia', '8', 'A', 83),
    ('Yamini Awasthi', '10', 'A', 92),
    ('Trisha Gera', '7', 'A', 77),
    ('Ritika Bansal', '9', 'C', 69),
    ('Garima Pathak', '8', 'C', 82),
    ('Shrishti Agrawal', '10', 'C', 87),
    ('Nandini Bhatia', '8', 'B', 76),
    ('Muskan Mahajan', '9', 'A', 73),
    ('Charvi Sood', '10', 'B', 89)
]

cursor.executemany('INSERT INTO STUDENT VALUES (?, ?, ?, ?)', students)
connection.commit()  # Save the changes

# Display the data in the table
print("\nThe inserted data is:")
data = cursor.execute('SELECT * FROM STUDENT')
for row in data:
    print(row)

connection.close()
