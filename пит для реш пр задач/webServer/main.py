from http.server import HTTPServer, CGIHTTPRequestHandler
import os, sys

# Путь до корня, где лежит cgi-bin
webdir = r'/Users/macos/PycharmProjects/edu/venv'
os.chdir(webdir)
srvaddr =("", 8000)
srvrobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()