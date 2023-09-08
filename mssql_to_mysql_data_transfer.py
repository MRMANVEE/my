import pyodbc 
import mysql.connector

mssql_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=your_server;DATABASE=your_database;Userid=your_username;password=your_password')

mysql_conn = mysql.connector.connect(
    host = "",
    user_name = "",
    password = "",
    database_name = ""
)


mssql_cursor = mssql_conn.cursor()
mssql_query = "select * from table_name_here"
mssql_cursor.execute(mssql_query)
mssql_data = mssql_cursor.fetchall()

mysql_cusor = mysql_conn.cursor()
mysql_query = "insert into table_name (column1,column2,column3,column4,....) values (value1,value2,,value3,,value4)"
for row in mssql_data:
    mysql_cusor.execute(mysql_query, row)
mysql_conn.commit()

mssql_cursor.close()
mssql_conn.close()

mysql_cusor.close()
mysql_conn.close()