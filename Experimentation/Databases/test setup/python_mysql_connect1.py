import mysql.connector
from mysql.connector import Error


def connect():
    try:
        conn = mysql.connector.connect(host='localhost', database='python_mysql', user='testuser2', password='')
        if conn.is_connected():
            print('Connected!')
            conn.close()
    except Error as e:
        print(e)


if __name__ == '__main__':
    connect()
