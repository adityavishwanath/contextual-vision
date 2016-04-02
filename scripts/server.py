#!/usr/bin/env python

import os
os.system("chmod +x server.py")
os.system("chmod +x cgi_module_prescription.py")
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; 

log_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'logs'))
#print log_dir

cgitb.enable(display=0, logdir=log_dir)  

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
httpd.serve_forever()