#!C:\Users\perig\AppData\Local\Programs\Python\Python311\python.exe
# registe.py

print("Content-Type: text/html")    # Generates HTTP header
print()                             # Blank line

# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
nm=form.getvalue('name')
gnd=form.getvalue('gender')
course=form.getvalue('course')
mob=form.getvalue('mobile')

# Generate the HTML content
print('<html>')
print('<body>')
print('<h2>Data received from Client browser with POST method.</h2>')
print('<b>Name: </b> {}</br>'.format(nm))
print('<b>Gender: </b> {}</br>'.format(gnd))
print('<b>Course: </b> {}</br>'.format(course))
print('<b>Mobile No: </b> {}</br>'.format(mob))
print('</body>')
print('</html>')
