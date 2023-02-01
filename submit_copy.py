#!/opt/homebrew/bin/python3

# Libraries Declaration

import pwd
from unittest import result
from urllib import response
import mysql.connector
import cgi
from fpdf import FPDF
import matplotlib.pyplot as plt , mpld3
from matplotlib.patches import ConnectionPatch
import numpy as np
import sys

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print('<meta charset="UTF-8">')
print('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print ('<title> WCAG 2.1 QUICK REFERENCE CRITIRIONS </title>')
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link type="text/css" rel="stylesheet" href="css1.css" />') 
print('<script src="script.js">''</script>')   
print ('</head>')
print ('<body>') 

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DHE"
)

form = cgi.FieldStorage()
tvalue0 = form.getvalue("Record")
tvalue = form.getvalue("Surmane")
tvalue1 = form.getvalue("Name")
tvalue2 = form.getvalue("Rank")
tvalue3 = form.getvalue("Pemit")
tvalue4 = (form.getvalue("Duration"))
tvalue5 = ('30')


cursor=conn.cursor()   
selectquery1="insert into Persons (Record,Surmane, Name, Rank,Pemit,Duration,full,rest) values ('"+tvalue0+"','"+tvalue+"','"+tvalue1+"','"+tvalue2+"','"+tvalue3+"','"+tvalue4+"','"+tvalue5+"',full-Duration)"
cursor.execute(selectquery1) 


 
selectquery="select * from Persons"
cursor.execute(selectquery)

records=cursor.fetchall()
for row in records:
    print("Record",row[0])
    print("Surmane",row[1])
    print("Name",row[2])
    print("Rank",row[3])
    print("Penit",row[5])
    print("Duration",row[6])
    print("rest",row[8])
    print('</br>')    
   



cursor=conn.cursor() 
conn.commit()
conn.close()


#mpld3.show()    

print ('</body>')
print ('</html>')    


 


