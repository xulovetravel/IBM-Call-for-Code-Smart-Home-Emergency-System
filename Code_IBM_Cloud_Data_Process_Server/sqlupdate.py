#!/usr/bin/python
#!coding=utf-8
import pymssql
import datetime
print('Connect to the Datebase....')
#Connecting to SQL server by using system administrator account for Microsoft SQL Server.
conn = pymssql.connect(host='localhost', user='sa', port='1433', password = 'tofel100', database='SMART_HOME_EMERGENCY')

#Checking if connection is successful or not.
cursor = conn.cursor()
if not cursor:
    raise(NameError,'connect failed')
else:
    print('successful')



sql = "select * from messager"
cursor.execute(sql)
good = cursor.fetchall()
cursor.execute('''
    INSERT INTO messager ([Latitude]
      ,[Longitude]
      ,[Address_locate]
      ,[Floor_locate]
      ,[Resident]
      ,[Thermal Digital Details]
      ,[Voice_Details]
      ,[Message Sent time]
      ,[Postal Code]
      ,[Number of Victims]
      ,[row_id]
    )
    VALUES
    ('45.341788', '-75.690334', '3755 Riverside Drive, Ottawa', '10th', 'Zack, Bob', '[0 , 0, 0 ,0]', 'I need help!', '2019-06-20 10:00:00', 'K1V 1B8', 233, 1),
    ('45.339445', '-75.711996', '280 West Hunt Club Road, Ottawa', '1st', 'Jacob, Jason', '[254, 100, 49]', 'Help! I am stuck inside the restaurant!', '2019-06-18 07:00:00',  'K2E 0B7', 123, 2),
    ('45.322253', '-75.667521', '1000 Airport Parkway Private, Ottawa', '2nd', 'Ryan, Kim', '[129, 88, 12]', 'I am now stuck at the airport, help.', '2019-06-19 12:00:00', 'K1V 9B4', 422, 3),
    ('45.334167', '-75.690270', '224 Hunt Club Road, Ottawa', '1st', 'Yang, Bob', '[123, 16, 75]', 'Supermarket is falling aaprt, HELP!', '2019-06-20 19:30:00', 'K1V 1C1', 2 ,4),
    ('45.339618', '-75.686353', '1 Hunt Club Road, Ottawa', '1st', 'Ford, Mark', '[125, 14, 14]', 'Golf Club is not functioning, HELP!', '2019-06-19 18:30:00',  'K1V 1B9', 8, 5),
    ('45.344995', '-75.692094', '3635 Rivergate Way, Ottawa', '1st', 'Aziz, Nick', '[128, 12, 13]', 'Lights broke down, HELP!', '2019-06-19 17:00:00', 'K1V 2A4', 31, 6),
    ('45.340354', '-75.694562', '44 Kimberwick Crescent, Ottawa', '2nd', 'Tang, Nina', '[124, 13, 16]', 'I am stuck under the house, SOS!', '2019-06-18 15:00:00', 'K1V 0W7', 5, 7),
    ('45.341860', '-75.702267', '38 Rideau Heights Drive, Ottawa', '1st', 'Ches, Jim', '[126, 14, 15]', 'I am at the park under the mud', '2019-06-19 14:00:00', 'K2E 7A6', 4, 8),
    ('45.338049', '-75.715595', '310 West Hunt Club Road, Ottawa', '1st', 'Gues, Tim', '[123, 14, 51]', 'I have no where to hide, sos', '2019-06-20 13:15:00', 'K2E 0B7', 122, 9),
    ('45.331188', '-75.705654', '38 Auriga Drive, Ottawa', '2nd', 'Lee, Tom', '[125, 12, 14]', 'I am under the thick piles of cardboards, help', '2019-06-19 18:45:00', 'K2E 8A5', 4, 10)
    '''
    )
#Print the updated result after inserting the 2 data of rows without commiting on the SQL Server.
for row in good:
    print (row)

#conn.commit()is only used when I wanted to update the data onto the table.
#conn.commit()
    
conn.rollback()
#connection disconnected
conn.close()

