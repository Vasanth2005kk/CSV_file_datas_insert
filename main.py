# package install command !

# pip install mysql-connector-python
# pip install pandas

import pandas as pd
import mysql.connector 


# Step 1: Read the CSV file
csv_file_path = 'datas.csv'
data = pd.read_csv(csv_file_path)


# Step 2: Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ex"
)
cursor = conn.cursor()


# Step 3: Create an insert query template
table_name = 'inser_datas'
columns = ', '.join(data.columns)
placeholders = ', '.join(['%s'] * len(data.columns))
insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

# Step 4: Insert each row
for _, row in data.iterrows():
    cursor.execute(insert_query, tuple(row))

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()




#
'''
import mysql.connector
import pandas as pd

# Step 1: Read the CSV file
csv_file_path = 'datas.csv'
data = pd.read_csv(csv_file_path)

mysql_connection=
def insert(model,engine_power,age_in_days,km,previous_owners,lat,lon,price):

    responce=mysql_connection.cursor()

    query="insert into inser_datas(model,engine_power,age_in_days,km,previous_owners,lat,lon,price) values (%s,%s,%s,%s,%s,%s,%s,%s);"
    
    arugument_passing_column=(model,engine_power,age_in_days,km,previous_owners,lat,lon,price)
    
    responce.execute(query,arugument_passing_column)
    mysql_connection.commit()
    
    return "insert successfully".upper()


for _,row in data.iterrows():
    a = tuple(row)
    insert(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7])

'''