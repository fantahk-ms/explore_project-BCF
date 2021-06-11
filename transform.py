# test
# import pymysql
import pandas as pd
import pyodbc
# import socket

# socket.getaddrinfo('127.0.0.1', 8080)

print(pyodbc.drivers())

dbcon = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
'Server=explorer-interns;'
'Database=explorer;'
'Trusted_Connection=yes;')
cursor = dbcon.cursor()

try:
    SQL_Query = pd.read_sql_query(
        'SELECT * FROM explorer.dbo.Support', dbcon)

    df = pd.DataFrame(SQL_Query, columns=['Title', 'UserDescription'])
    print(df)
    print('The data type of df is: ', type(df))
except:
    print("Didn't work")

dbcon.close()


# ask tyrone about hostname
