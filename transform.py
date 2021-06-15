# test
# import pymysql
import pandas as pd
import pyodbc
from nltk.tokenize import word_tokenize
# import socket

# socket.getaddrinfo('127.0.0.1', 8080)

# print(pyodbc.drivers())

server = 'explorer-interns.database.windows.net'
database = 'explorer'
username = 'explorer'
password = 'expl@rerint@rns@1'

dbcon = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, autocommit = True)
cursor = dbcon.cursor()

SQL_Query = pd.read_sql_query(
    'SELECT * FROM explorer.dbo.Support', dbcon)

df = pd.DataFrame(SQL_Query, columns=['Title', 'UserDescription'])
    # print(df)
    # print('The data type of df is: ', type(df))

data_list = [df.columns.values.tolist()] + df.values.tolist()



print(data_list)


dbcon.close()


# ask tyrone about hostname


# TEST TEST TEST
