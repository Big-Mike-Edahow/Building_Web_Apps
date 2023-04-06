# big_mikes_wsgi_server.py
# A python script to implement a simple Web Server Gateway Interface

from wsgiref.simple_server import make_server

def application(environ, start_response):
    host=environ.get('HTTP_HOST')
    start_response("200 OK", [("Content-type", "text/html")])
    ret = [("<h2>Hello World!<br/>From Big Mikes WSGI Server: %s</h2>" % (host)).encode("utf-8")]
    return ret

server = make_server('localhost', 8000, application)

print ("Serving HTTP on port 8000...")

server.serve_forever()


