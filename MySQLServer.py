#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error
import sys

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2019'  # Replace with your password
        )

        if connection.is_connected():
            try:
                cursor = connection.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as db_err:
                print(f"Failed to execute query: {db_err}")
                sys.exit(1)
            finally:
                if 'cursor' in locals():
                    cursor.close()
        else:
            print("Connection to MySQL server failed.")
            sys.exit(1)

    except Error as conn_err:
        print(f"Connection error: {conn_err}")
        sys.exit(1)

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
