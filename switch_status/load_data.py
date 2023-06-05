import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='switch_data',
        user='root',
        password='password'
    )
    if connection.is_connected():
        print('Connected to MySQL database')

    csv_file = r'C:\Users\ainaa\PycharmProjects\pythonProject\switch_status\Data_Terminals.csv'
    df = pd.read_csv(csv_file)

    cursor = connection.cursor()
    for _, row in df.iterrows():
        switch_label = row['SW(Switch Lable)']
        terminal_1_status = row['T1(Terminal 1)']
        terminal_2_status = row['T2(Terminal 2)']
        terminal_3_status = row['T3(Terminal 3)']
        terminal_4_status = row['T4(Terminal 4)']
        terminal_5_status = row['T5(Terminal 5)']
        timestamp = row['TS(Unix Timestamp)']
        datetime_obj = datetime.fromtimestamp(timestamp)
        sql = "INSERT INTO terminalstatus (switch_label, terminal_1_status, terminal_2_status, terminal_3_status, terminal_4_status, terminal_5_status, timestamp) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s)"

        # Execute the query with the converted timestamp value
        cursor.execute(sql, (
            switch_label, terminal_1_status, terminal_2_status, terminal_3_status, terminal_4_status, terminal_5_status,
            datetime_obj))

        # Commit the changes to the database
        connection.commit()

    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print('Data inserted into MySQL database')

except Error as e:
    print(f'Error while inserting data into MySQL: {e}')

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
    print('MySQL connection closed')