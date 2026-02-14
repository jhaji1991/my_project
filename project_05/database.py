import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="testpydb"
        )
        return connection
    except Error as e:
        print(f" Database connection error: {e}")
        return None

def create_table():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                subject_name VARCHAR(255),
                question_text TEXT,
                answer_options TEXT,
                chapter_name VARCHAR(255)
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()

def insert_question(subject, question_text, answer_options, chapter):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO questions (subject_name, question_text, answer_options, chapter_name)
                VALUES (%s, %s, %s, %s)
            """, (subject, question_text, answer_options, chapter))
            connection.commit()
        except Error as e:
            print(f"Insert error: {e}")
        finally:
            cursor.close()
            connection.close()