__author__ = "navodissa"

from http.server import BaseHTTPRequestHandler,HTTPServer,socketserver

PORT_NUMBER = 8080

#This class will handle any incoming request from the browser

class myHandler(BaseHTTPRequestHandler):
	"""docstring for myHandler"BaseHTTPRequestHandlerf __init__(self, arg):"""
	# Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		#Send the HTML messages
		self.wfile.write(bytes("Hello", 'UTF-8'))
		return

try:
	#Create a web server and define the handler to manager the incoming request
	server = HTTPServer(('',PORT_NUMBER), myHandler)
	print ("Started httpserver on port", PORT_NUMBER)

	#Wait forever for incoming http requests
	print ("Server in listening state")
	server.serve_forever()

except KeyboardInterrupt:
	print ("^C received, shutting down the web server")
	server.socket.close()
