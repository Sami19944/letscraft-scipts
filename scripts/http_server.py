from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import os
import logging
import configparser
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()


        # Send message back to client
        message = "do_GET"
        message = message + '\n' + '<form action="" id="post">'
        message = message + '\n' + '   <input type="text" name="func">'
        message = message + '\n' + '   <button type="submit">send</button>'
        message = message + '\n' + '</form>'
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())

 
def run(dev):
	create_logger()
	config_file = "main.conf"
	config = configparser.ConfigParser()
	config.read(config_file)
	print('http_server run')
	path = os.getcwd()
	print("   config_file:" + config_file)
	print("   path:" + path)
	print("   config")
	host = config['http_server']['host']
	print("       host: " + host)
	port = int(config['http_server']['port'])
	print("       port: " + str(port))
 
	print('   starting server...')
	# Server settings
	# Choose port 8080, for port 80, which is normally used for a http server, you need root access
	server_address = (host, port)
	httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
	print('   running server...')
	httpd.serve_forever()

def create_logger():
	# Create a custom logger
	logger = logging.getLogger(__name__)

	# Create handlers
	c_handler = logging.StreamHandler()
	c_handler.setLevel(logging.DEBUG)
	f_handler = logging.FileHandler(__name__ + ".log")
	f_handler.setLevel(logging.DEBUG)

	# Create formatters and add it to handlers
	c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
	f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	c_handler.setFormatter(c_format)
	f_handler.setFormatter(f_format)

	# Add handlers to the logger
	logger.addHandler(c_handler)
	logger.addHandler(f_handler)