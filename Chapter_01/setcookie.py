#!C:\Users\perig\AppData\Local\Programs\Python\Python311\python.exe
# setcookie.py

# Import the SimpleCookie class as defined in the http.cookies module
from http import cookies

# Create the cookies
c = cookies.SimpleCookie()
c ['userID'] = 'admin'
c ['pwd'] = '1234'

# Print the HTTP header, starting with the cookie
print (c)
print ("Content-type: text/html\n")
print ("")

htm = """
<html>
<body>
<h1>The cookie has been set</h1>
</body>
</html>
"""

print (htm)
