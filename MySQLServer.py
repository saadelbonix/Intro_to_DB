#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust credentials if necessary)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2019'
        )

        if connection.is_connected():
            try:
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as db_err:
                print(f"Error executing SQL statement: {db_err}")
            finally:
                if 'cursor' in locals():
                    cursor.close()

    except Error as conn_err:
        print(f"Error connecting to MySQL server: {conn_err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
