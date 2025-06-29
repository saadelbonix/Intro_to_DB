#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (change credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2019'  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL or creating database: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
