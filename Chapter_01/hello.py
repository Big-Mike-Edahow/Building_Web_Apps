#!C:\Users\perig\AppData\Local\Programs\Python\Python311\python.exe
# hello.py

print("Content-Type: text/html")    #generates HTTP header
print()                             #blank line

print ('<html>')
print ('<head>')
print ('<title>Big Mikes First CGI Program</title>')
print ('<style>body { background-color: lightskyblue; }</style>')
print ('</head>')
print ('<body>')
print ('<img src=\"https://big-mike-edahow.github.io/images/Profile_Picture.jpg\" height=\"240px\"; width=\"320px\";>')
print ('<h2>Hello World!</h2>')
print ('<h2>This is Big Mikes first CGI Script in Python.</h2>')
print ('<h4>I\'m reading the book Building Web Apps with Python and Flask.</h4>')
print ('<h4>I\'m running the Apache Web Server.</h4>')
print ('</body>')
print ('</html>')
