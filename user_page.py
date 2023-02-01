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
import requests
import webbrowser



print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print('<link type="text/css" rel="stylesheet" href="css1.css" />') 
print('<script src="script3.js">''</script>') 
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print ('<title> WCAG 2.1 QUICK REFERENCE CRITIRIONS </title>')
print('<meta name="viewport" content="width=device-width, initial-scale=1">')

#print('<script src="script.js">''</script>')   
print ('</head>')

print('<meta charset="UTF-8">')
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="DHE"
)

form = cgi.FieldStorage()
tvalue = form.getvalue("user")
tvalue1 = form.getvalue("pass")
tvalue4 = form.getvalue("txtInput")
tvalue5 = form.getvalue("mainCaptcha")    
tvalue2 = "user"
tvalue3 = "123"
if ((tvalue == tvalue2) and (tvalue1 == tvalue3) and (tvalue4 == tvalue5)):
      print("OK")
      webbrowser.open('http://localhost/codeMcs/index2.html')
      cursor=conn.cursor()   
      selectquery1="insert into Validation(user, pass ) values ('"+tvalue+"','"+tvalue1+"')"
      cursor.execute(selectquery1) 
      cursor=conn.cursor() 
      conn.commit()
elif ((tvalue == tvalue2) and (tvalue1 == tvalue3) and (tvalue4 != tvalue5)): 
      print('<body>') 
      print('jfdksjbskjvbkjsnvb')    
      webbrowser.open('http://localhost/codeMcs/login.html') 
      print('</body>')     
    
else:
      print("Wrong Validation")
      print ('<form action = "http://localhost/codeMcs/login.html"method = "POST" class ="form">')      
      print('<button class="button">Back</button>')

conn.close()








#mpld3.show()

print ('</html>')    


 


