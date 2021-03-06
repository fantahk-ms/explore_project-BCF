# test
# import pymysql
import pandas as pd
import pyodbc
# import socket

# socket.getaddrinfo('127.0.0.1', 8080)

# print(pyodbc.drivers())

server = 'explorer-interns.database.windows.net'
database = 'explorer'
username = 'explorer'
password = 'expl@rerint@rns@1'

dbcon = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password, autocommit = True)
cursor = dbcon.cursor()

SQL_Support = pd.read_sql_query(
    'SELECT * FROM explorer.dbo.Support', dbcon)

SQL_train = pd.read_sql_query(
    'SELECT * FROM explorer.dbo.Training', dbcon)

SQL_test = pd.read_sql_query(
    'SELECT * FROM explorer.dbo.Testing', dbcon)

SQL_cluster = pd.read_sql_query(
    'SELECT * FROM explorer.dbo.ClusterData', dbcon)

SQL_process = pd.read_sql_query(
    'SELECT * FROM explorer.dbo.TicketData722', dbcon)    

df_support = pd.DataFrame(SQL_Support, columns=['Title', 'UserDescription'])
    # print(df)
    # print('The data type of df is: ', type(df))
df_training = pd.DataFrame(SQL_train, columns=['SubArea', 'Title', 'UserDescription'])

df_testing = pd.DataFrame(SQL_test, columns=['Title', 'UserDescription'])

df_cluster = pd.DataFrame(SQL_cluster, columns=['Title', 'UserDescription'])

df_process = pd.DataFrame(SQL_process, columns=['Category', 'Platform', 'Ticket'])

support_list = [df_support.columns.values.tolist()] + df_support.values.tolist()

training_list = [df_training.columns.values.tolist()] + df_training.values.tolist()

testing_list = [df_testing.columns.values.tolist()] + df_testing.values.tolist()

cluster_list = [df_cluster.columns.values.tolist()] + df_cluster.values.tolist()

process_list = [df_process.columns.values.tolist()] + df_process.values.tolist()





# print(training_list)
# print("\n")
# print(testing_list)

dbcon.close()


# ask tyrone about hostname


# TEST TEST TEST
