import mysql.connector
import pyodbc


#class SQLconnect:
    #server = '127.0.0.1'
    #database = 'topDB'
    #username = 'root'
    #password = ''
    #driver= '{ODBC Driver 17 for SQL Server}'
    #cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=3380;DATABASE='+database+';UID='+username+';PWD='+ password)
    #cursor = cnxn.cursor()

def Statement(statement,values,conn,cursor):

    cursor.execute(statement,values)
    conn.commit()
