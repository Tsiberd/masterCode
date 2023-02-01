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
tvalue = form.getvalue("user")
cursor=conn.cursor()   

selectquery="select * from Persons where Record = '"+tvalue+"'"
cursor.execute(selectquery)

records=cursor.fetchall()
for row in records:
    print("Surmane",row[0])
    print("Name",row[1])
    print("Rank",row[3])
    print("Penit",row[5])
    print("Duration",row[6])
    print("rest",row[8])
    print('</br>')    
   


cursor=conn.cursor() 
conn.commit()
conn.close()


print ('</body>')
print ('</html>')    


 


