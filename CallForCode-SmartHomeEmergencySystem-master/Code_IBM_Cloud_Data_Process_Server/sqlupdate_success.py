#!/usr/bin/python
#!coding=utf-8
import pymssql
import datetime
import urllib.request, json 
import time
#added while loop to be able to update automatically to deliver the help information
while True:
    with urllib.request.urlopen("https://smart-home-dc098.firebaseio.com/command.json") as url:
        data = json.loads(url.read().decode())
        print(data['VoiceCommand'])

    firebasecontent=data['VoiceCommand']

    ##############Connecting to SQL#######################
    #print('Connect to the Datebase....')
    #Connecting to SQL server by using system administrator account for Microsoft SQL Server.
    conn = pymssql.connect(host='localhost', user='sa', port='1433', password = 'tofel100', database='SMART_HOME_EMERGENCY')

    #Checking if connection is successful or not.
    cursor = conn.cursor()
    if not cursor:
        raise(NameError,'connect failed')
    else:
        print('successful')


    #New column to represent how many people.
    sql = "select * from messager"
    cursor.execute(sql)
    good = cursor.fetchall()
    #Wanted to update the message.
    sql_query="""UPDATE messager
                 SET Voice_Details = %s
                 WHERE row_id = 1
                 """
    Voice_Details=firebasecontent
    input = Voice_Details
    cursor.execute (sql_query, input)

    #Print the updated result after inserting the 2 data of rows without commiting on the SQL Server.
    for row in good:
        print (row)

    #conn.commit()is only used when I wanted to update the data onto the table.
    conn.commit()
    
    conn.rollback()
    #connection disconnected
    conn.close()
    #set 2 seconds for the refresh.
    time.sleep(2)

