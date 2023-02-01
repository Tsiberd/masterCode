#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

from os import linesep
from typing import ValuesView
from bs4 import BeautifulSoup, element
import cgi, cgitb
from nltk import tag
from requests.api import get
cgitb.enable()
from bs4.builder import SAXTreeBuilder
import nltk
import requests
import re
#from PIL import Image
from xml.dom import IndexSizeErr, minidom
import speech_recognition as speech_recog
import time
import js2py



with open("index2.html" , "r") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print ("<h2> You gave the url %s </h2>" % given_url)
result =soup.find("label") 
result2 = soup.find("input")
print ("result['for']: " , result['for'])
print(tags2)
print(tags)
print ("result2['id']: " , result2['id'])
#if (result['for']==result2['id']):
 #   print('Ok')
#else:
 #   print('wrong')
#  print('<button onclick="myfunction">Press Me</button>')
#print('<label name="home" onmouseover="Mouseover(this);" onmouseout =" Mouseout(this);">clickMe')       
#print('soup.pretiffy()')
#print(soup.prettify())
#print('<input title="Search" type="text" name="search">')
#print('<button type="submit">Submit</button>')  """
#print('<div id="MyDIV">"kdjfsljf"</div>')
print ('<html>')
print ('<head>')
print('<meta charset="UTF-8">')
print('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print ('<title>Hello World - First CGI Program</title>')
print('<meta name="viewport" content="width=device-width, initial-scale=1">')
print('<link type="text/css" rel="stylesheet" href="css1.css" />') 
print('<script src="script.js"></script>')   
print ('</head>')
print ('<body>') 
print ('</body>')
print ('</html>') 