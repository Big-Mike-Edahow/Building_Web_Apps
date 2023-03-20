#!C:\Users\perig\AppData\Local\Programs\Python\Python311\python.exe
# readcookies.py

# Import the SimpleCookie class as defined in the http.cookies module
from http import cookies

# The os module provides a portable way of using operating system dependent functionality.
import os

print("Content-Type: text/html")    #generates HTTP header
print()                             #blank line

htm = """
<html><body><h1>Read the cookies</h1>
"""
print (htm)

if 'HTTP_COOKIE' in os.environ:
    cookie_string = os.environ.get('HTTP_COOKIE')
    c = cookies.SimpleCookie()
    c.load(cookie_string)

for cookie in map(str.strip, str.split(cookie_string, ';')):
    (key, value) = str.split(cookie, '=')
    print ("<b>Name</b>:{} <b>Value</b>:{}".format(key,value))
    print ("<br/>")

print ('</body></html>')
