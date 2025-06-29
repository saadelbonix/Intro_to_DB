#!/usr/bin/env python3

import mysql.connector
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
            except mysql.connector.Error as err:
                print(f"Failed to execute query: {err}")
                sys.exit(1)
            finally:
                if 'cursor' in locals():
                    cursor.close()
        else:
            print("Connection to MySQL server failed.")
            sys.exit(1)

    except mysql.connector.Error as err:
        print(f"Connection error: {err}")
        sys.exit(1)

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
